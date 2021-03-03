from django import forms
from .models import Post


class UserdataModelForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['headline']