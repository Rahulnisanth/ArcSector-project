from django import forms
from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'project_image', 'source_link', 'tags',
                  'start_date', 'completed_date', 'voucher')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your project title'}),
            'project_image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Select the project image'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your project description', 'rows': '4'}),
            'source_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your project demo-link'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Select the required tags'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter the project started date'}),
            'completed_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter the project completed date'}),
            'voucher': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Budget proposed'}),
        }
