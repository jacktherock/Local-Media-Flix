from django.shortcuts import render, redirect
from .forms import MediaForm
from .models import Media
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from decouple import config

# homepage
def homepage(request):
    return render(request, "homepage.html")

# about page
def about(request):
    return render(request, "about.html")

def privacypolicy(request):
    return render(request, "privacypolicy.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message
        }
        message = '''
        Message: {}
        
        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', [config('EMAIL')])
        messages.success(request, "Thank You For Contacting !")
    return render(request, "contact.html", {})
    

# view media
def mediaUser(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            # admin can view all uploaded media of all users
            media = Media.objects.all()
        else:
            media = Media.objects.filter(user=request.user)
        context = {"media": media}
        return render(request, "media.html", context)
    else:
        messages.error(request, "Please Login to Access Media !")
        return HttpResponseRedirect("/auth/auth/login/")

# upload media
def upload(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            file = MediaForm(
                request.POST, request.FILES, instance=Media(user=request.user)
            )
            if file.is_valid():
                profile = file.save(commit=False)
                profile.user = request.user
                profile.save()
                messages.success(request, "Media Uploaded Successfully !")
                return redirect("/upload/")
            else:
                messages.error(request, "Please Select Valid Media Files !")
        else:
            file = MediaForm()
        return render(request, "upload.html", {"files": file})
    else:
        return HttpResponseRedirect("/auth/auth/login/")

# delete media
def deleteMedia(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Media.objects.get(pk=id)
            pi.delete()
            messages.success(request, "Media Deleted Successfully !")
            return HttpResponseRedirect("/media/")
    else:
        return HttpResponseRedirect("/auth/auth/login/")

# admin can view all users
def allUsers(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            users = User.objects.all()
            return render(request, "allusers.html", {"users": users})
        else:
            messages.error(request, "Unauthorized User Can't Access This Page !")
            return redirect("/")
    else:
        return HttpResponseRedirect("/auth/auth/login/")

# admin can delete existing user
def delete_user(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            user = User.objects.get(pk=id)
            user.delete()
            return redirect("/authadmin/allusers/")
        else:
            messages.error(request, "Unauthorized User Can't Access This Page !")
            return redirect("/")
    else:
        return redirect("/auth/auth/login/")

