from django.shortcuts import render
from django.views.generic import ListView,DetailView
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