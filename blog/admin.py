from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost, Tag


class BlogPostAdmin(SummernoteModelAdmin):
    """blog post admin view model"""
    pass


class TagAdmin(admin.ModelAdmin):
    """tag admin view model"""
    pass


admin.site.register(Tag)
admin.site.register(BlogPost, BlogPostAdmin)
