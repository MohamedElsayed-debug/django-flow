from django.db import models

class FacebookToken(models.Model):
    token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class FacebookPost(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    posted = models.BooleanField(default=False)
