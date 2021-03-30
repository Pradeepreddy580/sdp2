from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm

class EditUserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields =['first_name','last_name','email']
