from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=221)
    slug = models.SlugField()
    genre = models.CharField(max_length=221)
    author = models.CharField(max_length=221)
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.title
