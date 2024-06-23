from django.contrib import admin
from .models import Photos


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'image')
