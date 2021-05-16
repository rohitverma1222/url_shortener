from django.shortcuts import render,redirect
import bitly_api
import requests

from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'index.html')
def short(request):
    token=['6fd1b212fe96d58f270326124ea6cc27b9acee2b']
    connection=bitly_api.Connection(access_token=token)
    url=request.POST['num1']
    if (url.find('http')==-1):
        messages.warning(request,'Enter Valid URL')
        return redirect('/')
    else:
        shorten_url=connection.shorten(url)
    return render(request,'index.html',{'shorten':shorten_url})
