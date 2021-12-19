from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , "pages/index.html")

def profile(request):
    return render(request , "pages/profile.html")

def login(request):
    return render(request , "pages/login.html")

def signup(request):
    return render(request , "pages/signup.html")

def inbox(request):
    return render(request , "pages/inbox.html")

def account(request):
    return render(request , "pages/account.html")     

def skill_form(request):
    return render(request , "pages/skill-form.html")

def user_form(request):
    return render(request , "pages/user-form.html")

def message_form(request):
    return render(request , "pages/message-form.html")