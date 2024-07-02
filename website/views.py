from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
	#check to see if logging in
	if request.method=='POST':
		username=request.POST['User_name']
		password=request.POST['password']
		#Authenticate
		user=authenticate(request,username='User_name',password='password')
		if user is not None:
			login(request,user)
			messages.success(request,"You have been logged in !")
			return redirect('home')
		else:
			messages.success(request,"There was an error logging in")
			return redirect('home')
	else:



	    return render(request,'home.html',{})

def logout_user(request):
	logout(request)
	messages.success(request,"You have been logged out...")
	return redirect('home')
def register_user(request):
	return render(request,'register.html',{})



