from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.



def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profilepage')
        else:
            messages.error(request,'Invalid username or password')

    return render(request,'Login/Login_page.html')


def logout_page(request):
    logout(request)
    messages.success(request, 'Logout Successful !')
    return redirect('loginpage')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'User already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
            else:
                user = User.objects.create_user(username= username,email=email,password=password)
                user.save()
                return redirect('profilepage')
        else:
            messages.error(request, "Password and Confirm Password didn't match!")
    return render(request,'Login/Sign_up_page.html')

def profile_page(request):
    return render(request,'Login/Profile_page.html')

