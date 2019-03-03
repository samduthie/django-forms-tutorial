from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=140)
    slug = models.SlugField(unique=True)

    image = models.FileField(
        upload_to='uploads/',
        null=True,
        blank=True,
    )

    content = models.TextField()

