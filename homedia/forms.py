from django import forms
from .models import Media

# """-------------------------- Media Form --------------------------"""
class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['title', 'thumbnail', 'video']
        labels = {
            'title':'Media Title',
            'thumbnail': 'Media Thumbnail',
            'video':'Select Media'
        }
        widgets= {
            'title' : forms.TextInput(attrs={'class':'form-control'}), 
            'thumbnail' : forms.FileInput(attrs={'class':'form-control'}), 
            'video' : forms.FileInput(attrs={'class':'form-control'}), 
        }
