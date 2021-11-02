from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('media/',views.mediaUser, name='media'),
    path('about/',views.about, name='about'), 
    path('contact/',views.contact, name='contact'),
    path('upload/', views.upload, name='upload'),
    path('delete/<int:id>/', views.deleteMedia, name='delete'),
    path('authadmin/deleteuser/<int:id>/', views.delete_user, name="deleteuser"),
    path('authadmin/deletecontact/<int:id>/', views.delete_contact, name="deletecontact"),
    path('authadmin/allusers/', views.allUsers, name='allusers'),
    path('authadmin/allcontacts/', views.allContacts, name='allcontacts'),
]
