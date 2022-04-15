from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=221)
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.title
