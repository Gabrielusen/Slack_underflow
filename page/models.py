from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse
# from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager


User = settings.AUTH_USER_MODEL


class PostQuestion(models.Model):
    """ Model for posting questions """
    title = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, max_length=250)
    created_on = models.DateTimeField('date published', auto_now_add=True)
    text_content = models.TextField()
    tags = TaggableManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_view', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class PostAnswer(models.Model):
    """ Model for answering questions"""
    question = models.ForeignKey(
        PostQuestion,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text_content = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    approved_comment = models.BooleanField(default=False)
    created_on = models.DateTimeField('published', auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return 'comment by {} on {}'.format(self.user, self.question)
