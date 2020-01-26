from django.db import models
from django.utils import timezone


class Post(models.Model):
"""
This is the model for the blog posts
"""

title = models.CharField(max_length=200)
content = models.TextField()
created_date = models.DateTimeField(auto_now_add=True)
published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
views = models.IntegerField(default=0)
tags = models.CharField(max_length=30, blank=True, null=True)
image = models.ImageField(upload_to="img", blank=True, null=True)


def __unicode__(self):
    return self.title




