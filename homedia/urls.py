from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('media/',views.mediaUser, name='media'),
    path('about/',views.about, name='about'), 
    path('contact/',views.contact, name='contact'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('delete/<int:id>/', views.deleteMedia, name='delete'),
]