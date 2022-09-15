from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserLogin,ProfileForm,UserRegister,DivErrorList
from .utils import searchprofile
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def profile(request):
    search_query,profiles= searchprofile(request)
    context={
        'title':'PROFILE | PAGE',
        'profiles':profiles,
        'search_query':search_query
    }
    return render(request,'users/profile.html',context)

@staff_member_required(login_url='user:login')
def editprofile(request):
    search_query = ''
    if request.GET.get('search'):
        search_query =request.GET.get('search')
    profiles =Profile.objects.filter(name__icontains=search_query)
    context={
        'title':'DATA | PAGE',
        'profiles':profiles
    }
    return render(request,'users/profile/editprofile.html',context)

@login_required(login_url='user:login')
def createprofile(request):
    profileforms= ProfileForm(request.POST or None,request.FILES or None)
    if request.method =='POST':
        if profileforms.is_valid():
            profileforms.save()
            return redirect('user:edit')
    context={
        'title':'CREATE | PAGE',
        'profileforms':profileforms
    }
    return render(request,'users/profile/createprofile.html',context)

@login_required(login_url='user:login')
def deleteprofile(request,deleteinput):
    profiles = Profile.objects.get(id=deleteinput)
    profiles.delete()
    return redirect('user:edit')

@login_required(login_url='user:login')
def updateprofile(request,updateinput):
    profiles= Profile.objects.get(id=updateinput)
    profileforms= ProfileForm(request.POST or None,request.FILES or None,instance=profiles)
    if request.method =='POST':
        if profileforms.is_valid():
            profileforms.save()
            return redirect('user:edit')
    context={
        'title':'CREATE | PAGE',
        'profileforms':profileforms
    }
    return render(request,'users/profile/createprofile.html',context)


def detailprofile(request,detailinput):
    profiles = Profile.objects.filter(slug=detailinput)
    context={
        'title':'MORE INFO | PAGE',
        'profiles':profiles,
    }
    return render(request,'users/profile/detailprofile.html',context)

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('home:index')
    forms = UserLogin(request.POST or None)
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            if user is not None:
                user =authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'login by {} successs'.format(username))
                    return redirect('home:index')
                else:
                    messages.error(request,'password is incorrect')
        except:
            messages.error(request,'username does no exist')
        
    context={
        'title':'LOGIN | PAGE',
        'forms':forms,
    }
    return render(request,'users/login.html',context)

def userlogout(request):
    logout(request)
    return redirect('user:login')

def userregister(request):
    userregisterforms=UserRegister(request.POST or None,error_class=DivErrorList)
    if request.method == 'POST':
        if userregisterforms.is_valid():

            userregisterforms.save()   
            messages.success(request,'register successs')
            return redirect('user:login')
        else:
            messages.error(request,'failed to register account')
    context={
        'title':"REGISTER | PAGE",
        'userregisterforms':userregisterforms
    }
    return render(request,'users/register.html',context)
