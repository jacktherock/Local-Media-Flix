from django.db import models
from django.contrib.auth.models import User

class Media(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    thumbnail = models.ImageField(upload_to='thumbnails', default="")
    title = models.CharField(max_length=1000, blank=True, default="")
    video = models.FileField(upload_to='files', default="")
    created_at = models.DateTimeField(auto_now_add=True)
