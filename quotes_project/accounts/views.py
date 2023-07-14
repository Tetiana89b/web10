from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotes_app:base')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes_app:base')
        else:
            return render(request, 'accounts/register.html', context={"form": form})

    return render(request, 'accounts/register.html', context={"form": RegisterForm()})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotes_app:base')

    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='accounts:login')

        login(request, user)
        return redirect(to='quotes_app:base')

    return render(request, 'accounts/login.html', context={"form": LoginForm()})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='quotes_app:base')
