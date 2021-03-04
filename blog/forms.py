from django import forms
import datetime

from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        now = datetime.datetime.now().date()
        model = Blog
        fields = ['title', 'date', 'blog_post', 'tags', 'is_public']
        widgets = {
            "date": forms.SelectDateWidget(
                attrs={
                    "value": now
                }
            )
        }
