from django import forms
from .models import Vpost

class PostForm(forms.ModelForm):

    class Meta:
        model = Vpost
        fields = ['text', 'cover']