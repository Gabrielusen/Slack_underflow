from django.contrib import admin
from .models import PostQuestion, PostAnswer


# class CommentInline(admin.TabularInline):
#    model = PostAnswer


class QuestionAdmin(admin.ModelAdmin):
    # inlines = [CommentInline, ]
    prepopulated_fields = {'slug': ('title',)}  # automatically generate slug


admin.site.register(PostQuestion, QuestionAdmin)
admin.site.register(PostAnswer)
