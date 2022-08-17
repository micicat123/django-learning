from dataclasses import field
from django import forms
from django.forms import ModelForm
from django.core import validators
from FirstApp.models import Webpage, AccessRecord, Topic, UserProfile
from django.contrib.auth.models import User

#because it takes value as argument djngo knwos its validation
def checkForZ(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with z")

#creating of form
class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profilePicture',)