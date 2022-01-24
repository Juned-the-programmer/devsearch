from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage


# Create your views here.
@login_required(login_url='login')
def index(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter( 
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query)|
        Q(skill__in=skills)
    )

    page = request.GET.get('page')
    result = 10
    paginator = Paginator(profiles , result)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    left_index = (int(page) - 4)
    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 5)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)


    context = {
        'profiles' : profiles,
        'search_query' : search_query,
        'custom_range' : custom_range
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

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not existed")
        
        user_login = auth.authenticate(username=username , password=password)
        if user_login is not None:
            auth.login(request,user_login)
            return redirect('index')
        else:
            messages.error(request, "Username or password is not valid")

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
    messages.success(request , "User Logout ! ")
    return redirect('login')

@login_required(login_url='login')
def inbox(request):
    return render(request , "pages/inbox.html")

@login_required(login_url='login')
def account(request):
    profile = request.user.profile
    context = {
        'profile' : profile
    }
    return render(request , "pages/account.html" , context)     

@login_required(login_url='login')
def skill_form(request):
    user = request.user.username
    skill = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = user
            skill.save()
            return redirect('account')

    context = {
        'skill' : skill
    }
    return render(request , "pages/skill-form.html" , context)

@login_required(login_url='login')
def update_skill(request,pk):
    skill_data = Skill.objects.get(id=pk)
    skill = SkillForm(instance=skill_data)

    if request.method == 'POST':
        form = SkillForm(request.POST , instance=skill_data)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        'skill' : skill
    }
    return render(request , "pages/skill-form.html" , context)

@login_required(login_url='login')
def delete_skill(request,pk):
    skill_data = Skill.objects.get(id=pk)

    if request.method == 'POST':
        skill_data.delete()
        return redirect('account')

    context = {
        'object' : skill_data
    }
    return render(request , "project/delete_object.html" , context)

@login_required(login_url='login')
def user_detail(request,pk):
    profile_info = Profile.objects.get(id=pk)
    
    form = ProfileForm(instance=profile_info)

    if request.method == 'POST':
        form = ProfileForm(request.POST , request.FILES , instance=profile_info)
        if form.is_valid():
            form.save()

        return redirect('account')

    context = {
        'form' : form
    }
    return render(request , "pages/user-form.html" , context)

@login_required(login_url='login')
def message_form(request):
    return render(request , "pages/message_form.html")