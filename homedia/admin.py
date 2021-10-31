from django.contrib import admin
from .models import Media, Contact

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id','user','title', 'thumbnail', 'video', 'created_at']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email', 'message']