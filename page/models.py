from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse


User = settings.AUTH_USER_MODEL


class PostQuestion(models.Model):
    """ Model for posting questions """
    title = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    text_content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class PostAnswer(models.Model):
    title = models.ForeignKey(
        PostQuestion,
        on_delete=models.CASCADE,
        related_name='postanswers',
    )
    slug = models.SlugField
    text_content = models.CharField(max_length=400)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.text_content

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
