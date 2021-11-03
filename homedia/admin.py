from django.contrib import admin
from .models import Media

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id','user','title', 'thumbnail', 'video', 'created_at']
