from django.contrib import admin
from .models import Image
from django.db.models import Count


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']
    images_by_popularity = Image.objects.order_by('-total_likes')
