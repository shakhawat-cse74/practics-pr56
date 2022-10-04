from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from .forms import SignupForm


# Signup view function
def user_signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created successfully')
            fm.save()
            fm = SignupForm()
    else:
        fm = SignupForm()
    return render(request,'enroll/signup.html',{'form':fm})



# Login View Function
def user_Login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname= fm.cleaned_data['username']
                upass= fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login (request,user)
                    messages.success(request,'Loged In Successfully!!!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'enroll/userlogin.html',{'form':fm})
    
    else:
        return HttpResponseRedirect('/profile/')


# Profile View Function
def user_Profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/userprofile.html',{'name': request.user})
    else:
        return HttpResponseRedirect('/login/')
    


# Logout view function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')