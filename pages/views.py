from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='login')
def index(request):
    profiles = Profile.objects.all()
    context = {
        'profiles' : profiles
    }
    return render(request , "pages/index.html" , context)

@login_required(login_url='login')
def profile(request,pk):
    profile = Profile.objects.get(id=pk)

    topskill = profile.skill_set.exclude(description__exact="")
    otherskill = profile.skill_set.filter(description="")

    context = {
        'profile' : profile,
        'topskill' : topskill,
        'otherskill' : otherskill
    }
    return render(request , "pages/profile.html",context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user_login = auth.authenticate(username=username , password=password)
        if user_login is not None:
            auth.login(request,user_login)
            return redirect('index')
        else:
            print("Login Error")

    return render(request , "pages/login.html")

def signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm-password"]

        if password == confirm_password:
            user_signup = User.objects.create_user(first_name=first_name,last_name=last_name, username=username,email=email, password=password)
            user_signup.save()
            return redirect('login')
        else:
            print("Password doesnot match")

    return render(request , "pages/signup.html")

def logout(request):
    auth.logout(request)
    return redirect('index')

@login_required(login_url='login')
def inbox(request):
    return render(request , "pages/inbox.html")

@login_required(login_url='login')
def account(request):
    profile = Profile.objects.get()
    context = {
        'profile' : profile
    }
    return render(request , "pages/account.html" , context)     

@login_required(login_url='login')
def skill_form(request):
    return render(request , "pages/skill-form.html")

@login_required(login_url='login')
def user_detail(request):
    return render(request , "pages/user-form.html")

@login_required(login_url='login')
def message_form(request):
    return render(request , "pages/message_form.html")