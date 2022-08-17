from atexit import register
from os import access
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from FirstApp.forms import UserProfileInfoForm, UserRegistrationForm  
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    myDict = {'text': "Hello World", 'number': 100}
    return render(request,'FirstApp/index.html', context=myDict)

def FirstAppView(request):
        return render(request,'FirstApp/firstapp.html')
    
def Register(request):
    registered = False
 
    if request.method == 'POST':
        userForm = UserRegistrationForm(data=request.POST)
        userInfo = UserProfileInfoForm(data=request.POST)

        if userForm.is_valid() and userInfo.is_valid():
            user = userForm.save()
            user.set_password(user.password)

            profile = userInfo.save(commit=False)
            profile.user = user
            if 'profilePicture' in request.FILES:
                profile.profilePicture = request.FILES['profilePicture']

            profile.save()
            registered = True
        else:
            print(userForm.errors, userInfo.errors)    
    else:
        userForm = UserRegistrationForm()
        userInfo = UserProfileInfoForm()        

    return render(request,'FirstApp/form.html', {'userForm': userForm, 'userInfo': userInfo, 'registred': registered})        

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print("Username:{} and password:{}".format(username, password))    
            return HttpResponse("Invalid login details!")        
    else:
        return render(request,"FirstApp/login.html")

@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))                