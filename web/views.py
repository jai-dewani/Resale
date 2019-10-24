from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model, logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
from .models import Item, Comment, UserAccount, Image

def index(request):
	if not request.user.is_authenticated:
		return redirect('/loginuser')
	else:
		try:
			user = User.objects.get(user=request.user)
			context = {
				'user':user,
				'username':user.username
			}
			print(user)
		except:
			context = {}
		return render(request,'index.html',context)


def createItem(request):
	if request.method=='POST':
		user = UserAccount.objects.get(user=request.user)
		itemname = request.POST['itemname']
		description = request.POST['description']
		price = request.POST['price']
		# print("IMAGES",request.FILES['images'])
		images = request.FILES.getlist('images')
		# print("IMAGES",images)
		newItem = Item(
			user = user,
			itemName = itemname,
			description = description,
			price = price
		)
		newItem.save()
		for image in images:
			newImage = Image(
				item = newItem,
				image = image
			)
			newImage.save()

		return redirect('/')
	else:
		if not request.user.is_authenticated:
			return redirect('/loginuser')
		else:
			context = {}
			return render(request,'createItem.html',context)

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
		sem = request.POST['sem']
		phoneNumber = request.POST['phoneNumber']
		# try:
		user = User.objects.create_user(
			username = username,
			email=email,
			password=password
		)
		accountUser = UserAccount(
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
