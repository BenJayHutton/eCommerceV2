from django import forms
import datetime

from .models import Blog


class BlogForm(forms.ModelForm):
    #years = [(x) for x in range(1900, date.today().year + 1)]
    class Meta:
        now = datetime.datetime.now().date()
        year_range = tuple([i for i in range(now.year - 2, now.year + 3)])
        model = Blog
        fields = ['title', 'date', 'blog_post', 'tags', 'is_public']
        widgets = {
            "date": forms.SelectDateWidget(
                years=year_range,
                attrs={
                    "value": now
                }
            )
        }
