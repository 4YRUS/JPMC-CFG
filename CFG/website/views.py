from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import record2






def home(request):
	if request.user.is_authenticated:
		return render(request,'home.html',{})
	else:
		return redirect('login')

def user_login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		objects = record2.objects.all()
		for item in objects:
			if item.username == username:
				messages.success(request,item.role)
				place = item.role
		user=authenticate(request,username=username,password=password)
		if user:
			login(request,user)
			if place == 'DNR':
				return render(request,'home.html',{'role' : place})
			if place == 'WKR':
				return render(request,'leef.html',{'role' : place})
		return redirect('login')
	return render(request,'login.html',{})

