from django.db import models
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class Blog(models.Model):
    user        = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title       = models.CharField(max_length=120)
    blog_post   = models.TextField()
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email + " :- " + self.title
