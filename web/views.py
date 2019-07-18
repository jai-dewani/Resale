from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model, logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.


def index(request):
	if not request.user.is_authenticated:
		return redirect('/loginuser')
	else:
		context = {}
		return render(request,'index.html',context)


def loginview(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(
			request,
			username=username,
			password=password
		)
		if user is not None:
			login(request,user)
			print(user)
			return redirect('/')
		else:
			print("PROBLEM")
			context = {
				'message': 'Check login credentials'
			}
			return render(request,'login.html',context)
	else:
		return render(request,'login.html')


def signupview(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']
		phoneNumber = request.POST['phoneNumber']
		sem = request.POST['sem']
		# try:
		user = User.objects.create_user(
			username = username,
			email=email,
			password=password
		)
		accountUser = AccountUser(
			user = user,
			phoneNumber = phoneNumber,
			semester = sem
		)
		accountUser.save()
		user = authenticate(
			request,
			username=username,
			password=password
		)
		if user is not None:
			login(request,user)
			return redirect('/')
		else:
			print("PROBLEM")
			context = {
				'message': 'Check login credentials'
			}
			return render(request,'login.html',context)
	else:
		return render(request,'signup.html')


def logoutview(request):
	logout(request)
	return redirect('/')
