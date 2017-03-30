from django.shortcuts import render, HttpResponseRedirect
from .models import Treasure
from .forms import TreasureForm, LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def like_treasure(request):



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['name']
            p = form.cleaned_data['password']
            e = form.cleaned_data['email']
            user = User.objects.create_user(u, e, p)
            user.save()
            return HttpResponseRedirect('/')
        else:
            print "Wrong details"
    else:
        form = RegisterForm()
        return render(request, 'reg.html', {'form': form})

def index(request):
    treaures = Treasure.objects.all()
    form = TreasureForm()
    return render(request,'index.html',{'treaures':treaures, 'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print "The accoint is disabled"
            else:
                print "The user name is incorrect"
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})



def detail(request, tre_id):
    treaures = Treasure.objects.get(id=tre_id)
    return render(request,'detail.html',{'treaures':treaures})

def post_treasure(request):
    form = TreasureForm(request.POST, request.FILES)
    if form.is_valid():
        treasure = form.save(commit = False)
        treasure.user=request.user
        treasure.save()
    return HttpResponseRedirect('/')

def profile(request, username):
    user = User.objects.get(username=username)
    treaures = Treasure.objects.filter(user=user)
    return render(request,'profile.html',{"username":username,
                                          "treaures": treaures}
                 )





"""
link1 = "https://s-media-cache-ak0.pinimg.com/236x/4b/87/f4/4b87f4ed46a5d3edba956643915af524.jpg"
link2 = "https://s-media-cache-ak0.pinimg.com/236x/2e/c2/8d/2ec28d7f99c69b8f509f72122f072df6.jpg"
link3 = "https://s-media-cache-ak0.pinimg.com/236x/fc/b5/1c/fcb51cf6a50696b10b4b2014324b0126.jpg"
"""
