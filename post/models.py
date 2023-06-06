from django.db import models

from Social_Media_API import settings


class Hashtag(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    hashtag = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.content
