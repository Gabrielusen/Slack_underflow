from django.db import models
from django.utils.text import slugify
from django.conf import settings


User = settings.AUTH_USER_MODEL


class PostQuestion(models.Model):
    """ Model for posting questions """
    title = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    text_content = models.TextField()

    def __str__(self):
        return self.title
