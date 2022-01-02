from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, MyUserChangeForm, SignupForm
from authentication.forms import AdminCreateUserForm

# admin can create new user
def adminCreateUser(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                fm = AdminCreateUserForm(request.POST)
                if fm.is_valid():
                    fm.save()
                    messages.success(request, "New User Created Successfully !")
                    return redirect("/auth/admincreateuser/")
            else:
                fm = AdminCreateUserForm()
        else:
            messages.error(request, "Unauthorized User Can't Access This Page !")
            return redirect('/')
    else:
        return redirect("/auth/auth/login/")
    return render(request, "admincreateuser.html", {"form": fm})

# user profile
def userProfile(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = User.objects.get(pk=id)
            form = MyUserChangeForm(request.POST, instance=request.user)

            if form.is_valid():
                form.save()
                messages.success(request, "Profile Updated Successfully !")
        else:
            user = User.objects.get(pk=id)
            form = MyUserChangeForm(instance=request.user)
        context = {
            "form": form,
            "user": user,
        }
        return render(request, "userprofile.html", context)
    else:
        return HttpResponseRedirect("/auth/auth/login/")

# create new user
def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account created successfully! Please login !")
                return redirect("/auth/auth/login/")
        else:
            form = SignupForm()
        return render(request, "signup.html", {"form": form})
    else:
        messages.error(request, "You Already Logged In ! Please Logout to Create New Account !")
        return HttpResponseRedirect("/")

# login user
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data["username"]
                upass = fm.cleaned_data["password"]
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged In Successfully !")
                    return HttpResponseRedirect("/")
            # else:
            #     messages.error(request, "Username & Password are not matching ! Please try again or Create New Account !")
        else:
            fm = LoginForm(request=request)
        context = {"form": fm}
        return render(request, "login.html", context)
    else:
        messages.error(request, "You Already Logged In ! Please Logout to Login from another Account !")
        return HttpResponseRedirect("/")

# logout user
def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully !")
    return HttpResponseRedirect("/auth/auth/login/")
