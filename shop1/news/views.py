from django.shortcuts import render
from .models import Articles
# Create your views here.

def news_home(request):
    goods = Articles.objects.all()
    return render(request, 'main/news.html', {'news': goods})