from django.contrib import admin

# Register your models here.

from .models import Blog_post, Projects, Tag

admin.site.register(Blog_post)
admin.site.register(Projects)
admin.site.register(Tag)
