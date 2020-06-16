from django.contrib import admin
from .models import PostQuestion


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']


admin.site.register(PostQuestion, ArticleAdmin)
