from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView,DetailView
from django.contrib import messages
from .models import Mebel
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
            return render(request, 'buy_success.html', {'mebel': mebel})
        else:
            messages.error(request, 'Товар не в наличии!')
            return redirect('mebel-list')

    return render(request, 'buy_confirm.html', {'mebel': mebel})