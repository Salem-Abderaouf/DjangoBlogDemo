# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
# Create your views here.
def index(request):
    #return HttpResponse('Hello From Posts')
    posts = Posts.objects.all()[:10]
    context = {
        'posts': posts
    }
    return render(request,'posts/index.html' , context)

def details(request, id):
    det = Posts.objects.get(id=id)
    context = {
        'det' : det 
    }
    return render(request, 'posts/details.html' , context)

