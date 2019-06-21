from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Wish

# Create your views here.
class WishCreate(CreateView):
  model = Wish
  fields = ['title', 'description']

class WishDelete(DeleteView):
  model = Wish
  success_url = '/wishes/'

def home(request):
  return render(request, 'home.html')

def wishes_index(request):
  wishes = Wish.objects.all()
  return render(request, 'wishes/index.html', {'wishes': wishes})