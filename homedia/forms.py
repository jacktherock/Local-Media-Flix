from django import forms
from .models import Media, Contact

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

# """-------------------------- Contact Form --------------------------"""
class ContactForm(forms.ModelForm):
    class Meta:
        model =Contact
        fields = ['name', 'email', 'message']
        labels = {
            'name':'Enter Your Name',
            'email':'Enter Your Email ID',
            'message':'Enter Message / Apply for Local Account'
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Apply for an Local Account please provide First name, Last name, Email'}),
        }