from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView,DetailView
from django.contrib import messages
from .models import Mebel, Order
from django.contrib.auth import login
from .forms import RegisterForm
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request, 'index.html')
class MebelListView(ListView):
    model = Mebel
    template_name = 'catalog.html'
    context_object_name = 'mebel_list'

class MebelDetailView(DetailView):
    model = Mebel
    template_name = 'mebel_detail.html'
    context_object_name = 'mebel'


def buy_product(request, pk):
    mebel = get_object_or_404(Mebel, pk=pk)

    if request.method == 'POST':
        if mebel.quantity > 0:
            mebel.quantity -= 1
            mebel.save()
            if request.user.is_authenticated:
                Order.objects.create(
                    user=request.user,
                    mebel=mebel,
                    quantity=1,
                    price=mebel.price
                )
            return render(request, 'buy_success.html', {'mebel': mebel})
        else:
            messages.error(request, 'Товар не в наличии!')
            return redirect('mebel-list')

    return render(request, 'buy_confirm.html', {'mebel': mebel})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def map(request):
    return render(request, 'map.html')


def search_sql(request):
    query = request.GET.get('q', '')
    results = []
    sql_query = ""

    if query:
        sql_query = f"SELECT * FROM myapp_mebel WHERE title LIKE '%{query}%'"
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()

    return render(request, 'search_results.html', {
        'query': query,
        'results': results,
        'sql_query': sql_query,
    })

@csrf_exempt
def buy_no_csrf(request, pk):
    mebel = get_object_or_404(Mebel, pk=pk)

    if request.method == 'POST':
        if mebel.quantity > 0:
            mebel.quantity -= 1
            mebel.save()
            # === ЗАКАЗ СОЗДАЁТСЯ ===
            if request.user.is_authenticated:
                Order.objects.create(
                    user=request.user,
                    mebel=mebel,
                    quantity=1,
                    price=mebel.price
                )
            return render(request, 'buy_success.html', {'mebel': mebel})
        else:
            messages.error(request, 'Товар не в наличии!')
            return redirect('mebel-list')

    return render(request, 'buy_no_csrf.html', {'mebel': mebel})


@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order_detail.html', {'order': order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_orders.html', {'orders': orders})