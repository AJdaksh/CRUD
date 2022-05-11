from argparse import BooleanOptionalAction
from django.core import validators
from django import forms
from .models import user,signup,task

class dataadd(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
            'Description': forms.TextInput(attrs={'class':'form-control'}),
        }

class userform(forms.ModelForm):
    class Meta:
        model = signup
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }

class dataadd(forms.ModelForm):
    class Meta:
        model = task
        fields = '__all__'
        widgets = {
            'tasktitle': forms.TextInput(attrs={'class':'form-control'}),
            'duedate': forms.DateTimeInput(attrs={'class':'form-control'}),
            'status': forms.RadioSelect(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
        }