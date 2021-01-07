from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from store_account.functions import get_user_by_id

# Create your views here.
@login_required
def index(request):
    return render(request, 'store/account/index.html')

def login_page(request):
    if request.method == "POST":
        data = request.POST
        if data["type"] == "login":
            user = authenticate(request, username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful')
                if "next" in request.GET:
                    return HttpResponseRedirect(request.GET['next'])
                else:
                    return HttpResponseRedirect(reverse('account:index'))
            else:
                messages.error(request, "Invalid username or password")
        elif data["type"] == "signup":
            try:
                a = User.objects.get(username=data['username'])
            except:
                user = User()
                user.first_name = data["first_name"]
                user.last_name = data["last_name"]
                user.username = data["username"]
                user.email = data["email"]
                user.set_password(data["password"])
                user.save()
                u = authenticate(request, username=data["username"], password=data["password"])
                if u is not None:
                    login(request, u)
                    messages.success(request, "Welcome new user")
                    if "next" in request.GET:
                        return HttpResponseRedirect(request.GET['next'])
                    else:
                        return HttpResponseRedirect(reverse('account:index'))
            else:
                messages.error(request, "This username is already used")
    return render(request, 'store/account/login.html', {"user": request.user})

def forgot_password(request):
    context = {
        "change_for": False
    }
    if request.method == 'POST':
        if request.POST['type'] == 'user':
            try:
                user = User.objects.get(username=request.POST['username'])
            except:
                messages.error(request, 'User does not exist')
            else:
                context = {
                    "change_for": True,
                    "user": get_user_by_id(user.id)
                }
        elif request.POST['type'] == 'password':
            user = User.objects.get(pk=request.POST['user_id'])
            user.set_password(request.POST['password'])
            messages.success(request, 'Password successfully changed!')
            return HttpResponseRedirect(reverse('account:login'))
    return render(request, 'store/account/forgot-password.html', context)

def logout_user(request):
    logout(request)
    messages.info(request, 'You have successfully logged out!')
    return HttpResponseRedirect("/")