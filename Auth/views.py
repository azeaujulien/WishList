from django.conf.urls import url
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import resolve, reverse

from WishListDjango.views import index
from .models import Account, RegisterKey

from django.shortcuts import render, redirect
from .forms import UserCreationForm


def register_user(request):
    key = request.GET.get('key')
    try:
        key_obj = RegisterKey.objects.get(key=key)
    except RegisterKey.DoesNotExist:
        return render(request, "auth/register_error.html", {"error": "Register Key Not Found"})
    if request.method == 'POST':
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            key_obj.delete()
            return render(request, "auth/register_success.html")
        else:
            return render(request, "auth/register_error.html", {"error": form.errors})
    else:
        form = UserCreationForm()
    context = {"form": form, "key": key}
    return render(request, "auth/register.html", context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('Index')

    if request.method == 'POST':
        print(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(resolve(request.GET['next']).url_name)

        if len(Account.objects.filter(email=username)) == 0:
            context = {
                'username_error': "User not find for that email",
            }
        else:
            context = {
                'password_error': "Wrong password",
            }
    else:
        if 'next' in request.GET:
            context = {
                'next': request.GET['next']
            }
        else:
            context = {
                'next': reverse('Index')
            }
    return render(request, "auth/login.html", context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('Index')


@login_required
def get_current_user(request):
    context = {
        'user': request.user
    }
    return render(request, "auth/account.html", context)
