from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'DRAFT'
        PUBLISHED = 'PB','PUBLISHED'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', default=1)
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now) # дата публікації
    created = models.DateTimeField(auto_now_add=True)# дата створення
    update = models.DateTimeField(auto_now=True) # дата змінення
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title