from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)
    post = models.TextField()
    image = models.FileField(null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
