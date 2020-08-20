from django.contrib import admin
from .models import PostQuestion, PostAnswer
from tinymce.widgets import TinyMCE
from django.db import models
from .forms import PostForm
from pagedown.widgets import AdminPagedownWidget


class CommentInline(admin.TabularInline):
    model = PostAnswer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]
    prepopulated_fields = {'slug': ('title',)}  # automatically generate slug
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


class CommentAdmin(admin.ModelAdmin):
    # list_display = ('question', 'user', 'active', 'created_on')
    # list_filter = ('active', 'created_on')
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


admin.site.register(PostQuestion, QuestionAdmin)
admin.site.register(PostAnswer, CommentAdmin)
# admin.site.site_header = 'Pollster Admin'
# admin.site.site_title = ''
# admin.site.index_title = ''
