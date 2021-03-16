from django import forms
from .models import Post


"""
    defines the model form named UserdataModelForm
    the model creates a form of type post
    it excludes headline
    orders teh post in it ascending order
"""
class UserdataModelForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['headline']
        ordering = ['-date',]

    def clean(self):
        """cleans all the form data"""
        return self.clean()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserdataModelForm, self).__init__(*args, **kwargs)
