import re
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.forms import ModelForm
from accounts.models import Profile


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['UID','user']







