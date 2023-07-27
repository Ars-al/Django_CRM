from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
    # check if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        User = authenticate(request, username=username, password=password)
        if User is not None:
            login(request, User)
            messages.success(request, "You have been successfully logged in!")
            return redirect('home')
        else:
            messages.success(request, "Loggin in error, Please try again...")
            return redirect('home')
        
    else:
        return render(request, 'home.html', {})



def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully Logged out!")
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})