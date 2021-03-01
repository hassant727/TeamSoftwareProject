from django import forms
from .models import Userdata


class UserdataModelForm(forms.ModelForm):
    class Meta:
        model = Userdata
        exclude = ['headline']


