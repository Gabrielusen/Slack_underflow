from django.contrib import admin
from .models import PostQuestion, PostAnswer


class CommentInline(admin.TabularInline):
    model = PostAnswer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]
    prepopulated_fields = {'slug': ('title',)}  # automatically generate slug


class CommentAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'active', 'created_on')
    list_filter = ('active', 'created_on')


admin.site.register(PostQuestion, QuestionAdmin)
admin.site.register(PostAnswer)
