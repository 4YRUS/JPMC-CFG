from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import record2
from .forms import sign_up

global overallnames
overallnames = set()
overallnames.add('admin')



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
		place = ''
		for item in objects:
			if item.username == username:
				place = item.role
		user=authenticate(request,username=username,password=password)
		if user:
			login(request,user)

			if place == 'DONOR':
				return render(request,'home.html',{'role' : place})
			if place == 'GRASSROOT WORKER':
				return render(request,'leef.html',{'role' : place})
			if place == "":
				return user_logout(request)
		
	return render(request,'login.html',{})

def user_logout(request):
	logout(request)
	return redirect('login')




def register(request):
	if request.method=='POST':
		form=sign_up(request.POST)
		name = request.POST['username']
		role = request.POST['role']
		if name not in overallnames:
			member = record2(username = name,role= role)
		else:
			messages.success(request,'Username already Used')
			return redirect('register')	
			
		if form.is_valid():
			overallnames.add(name)
			form.save()
			member.save()
			messages.success(request,'User Created Succesfully...')
			return redirect('login')
		else:
			messages.success(request,'form invalid')
			
	else:
		form=sign_up()

	return render(request,'register.html',{'form':form})

def sponsor(request):
	if request.method=='POST':
		name = request.POST['name']
		email = request.POST['email']
		amount = request.POST['amount']
		return render(request,'done.html',{'data':[name,email,amount]})
	return render(request,'sponsor.html')