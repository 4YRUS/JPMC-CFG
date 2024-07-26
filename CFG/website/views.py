from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

def home(request):

	return render(request,'home.html',{})

def new(request):
	if request.method=='POST':
		message = request.POST.get("message")
		return render(request,'new.html',{'data':message})

























