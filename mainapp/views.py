from django.shortcuts import render
from .models import Photos


def index(request):
    photos = Photos.objects.all()
    return render(request, 'mainapp/index.html', context={
        'title': 'Home page',
        'photos': photos,
    })


def posts(request):
    photos = Photos.objects.all()
    return render(request, 'mainapp/posts.html', context={
        'title': 'All photo page',
        'photos': photos,
    })
