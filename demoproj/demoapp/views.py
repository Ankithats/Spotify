from django.shortcuts import render
from django.http import HttpResponse
from .models import Song
# Create your views here.
def home(req):
    data=Song.objects.all() 
    return render(req,'index.html',{'data':data})