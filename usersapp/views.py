from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login



# Create your views here.

def usersApp(request):

    if request.user.is_anonymous:
        return redirect('/login')

    return render(request, 'usersapp.html')

def loginUser(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
            
    


    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

