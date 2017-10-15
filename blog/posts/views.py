# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from .models import post
from .forms import ArticleForm, PostForm
# Create your views here.


def post_detail(request, pk):
    p = post.objects.get(pk=pk)
    return render(request, "posts/detail.html", {"post": p})

def post_list(request):
    posts = post.objects.all()
    
    return render(request, "posts/list.html", {"posts": posts})

def post_new(request):
#    form = ArticleForm(request.POST or None)
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        print form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list'))
        
    return render(request, "posts/new1.html",  {"form" : form})

    