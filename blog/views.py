#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""from django.shortcuts import render
from django.utils import timezone
from .models import Post #models.py'de yazdigimiz modeli ekleme
#fromdan sonraki nokta mevcut dizin veya mevcut uygulama anlamna geliyor. views.py ve models.py ayni dizinde olduklari icin sadece "."

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(yayinlanma_tarihi__lte=timezone.now()).order_by('yayinlanma_tarihi')     
    # yaynlanms ve yayinlanma_tarihine gore sralanms bir gönderi listesi
    #QuerySet imiz icin bir degisken yarattigimiza dikkat edin: posts. Bu QuerySetin ismi.
    return render(request, 'blog/post_list.html', {'posts': posts})"""

from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(yayinlanma_tarihi__lte=timezone.now()).order_by('yayinlanma_tarihi')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})