from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def goods(request):
    return render(request, 'main/goods.html')

