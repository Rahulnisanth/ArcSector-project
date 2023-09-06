from django.conf import UserSettingsHolder
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from user.forms import ProfileForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def homepage(request):
    return render(request, 'index.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'None registered user')
            return render(request, 'signin.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'OOPS! Something went wrong')
            return render(request, 'signin.html')

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('/')


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username):
                messages.error(request, 'Username already exists')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1)
                user.save()
                return redirect('signin')
        else:
            messages.error(request, 'OOPS! Check the Password')
            return render(request, 'register.html')

    return render(request, 'register.html')


def portfolio(request):
    return render(request, 'portfolio.html')


@login_required(login_url='signin')
def profile(request, pk):
    profile = Profile.objects.get(user=pk)
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


def edit_profile(request, pk):
    profile = Profile.objects.get(user=pk)
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {'form': form}
    return render(request, 'edit_profile.html', context)



@login_required(login_url='signin')
def designers(request):
    designers = Profile.objects.all()
    context = {'designers': designers}
    return render(request, 'designers.html', context)
