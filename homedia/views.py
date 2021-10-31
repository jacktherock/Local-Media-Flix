from django.shortcuts import render, redirect
from .forms import ContactForm, MediaForm
from .models import Media
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, "homepage.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        fm = ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Message Sent Successfully !")
    else:
        fm = ContactForm()
    return render(request, "contact.html", {"form": fm})


def mediaUser(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            media = Media.objects.all()
        else:
            media = Media.objects.filter(user=request.user)
        context = {"media": media}
        return render(request, "media.html", context)
    else:
        return HttpResponseRedirect("/login/")


class UploadView(View):
    def get(self, request):
        file = MediaForm()
        return render(request, "upload.html", {"files": file})

    def post(self, request):
        file = MediaForm(
            request.POST, request.FILES, instance=Media(user=self.request.user)
        )
        if file.is_valid():
            profile = file.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Media Uploaded Successfully !")
            return redirect("/upload/")
        return render(request, "upload.html", {"files": file})


def deleteMedia(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Media.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect("/media/")
    else:
        return HttpResponseRedirect("/login/")
