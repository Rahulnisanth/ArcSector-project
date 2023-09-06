from django import forms
from django.forms import ModelForm
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','name', 'first_name', 'last_name', 'country', 'occupation', 'DOB', 'mobile', 'email', 'bio','skills',
                'social_github', 'social_facebook', 'social_twitter', 'social_instagram', 'social_linkedin')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Country'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Occupation'}),
            'social_github': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Github Link'}),
            'social_facebook': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Facebook Link'}),
            'social_linkedin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Linkedin Link'}),
            'social_twitter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Twitter Link'}),
            'social_instagram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Instagram Link'}),
            'DOB': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Birthdate'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Years of Experience'}),
            'skills': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Mobile Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': '4','placeholder':'Enter a Short Description'}),
        }
