from django.contrib import admin
from .models import Post

# Register your models here.
# adminblog blog@gmail.com blog 12345

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
