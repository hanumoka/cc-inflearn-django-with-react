from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["caption", "location"]
        widgets = {
            "caption": forms.Textarea
        }
