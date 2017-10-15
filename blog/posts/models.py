# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    article_type = (
        ("POEM", "poem"),
        ("ARTICLE", "article"),
    )
    title = models.CharField("Title", max_length=250)
    content = models.TextField("Article")
    publish_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    author =  models.ForeignKey(User, related_name="blog_posts")
    post_image = models.FileField("Article_image", blank=True)
    article_type = models.CharField("Article Type", max_length=7, choices=article_type, default="POEM")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.id})
    
    
    class Meta:
        ordering = ["-publish_date"]