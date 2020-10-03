from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=200)
    body = models.TextField()
    picture = models.ImageField()
    demo = models.URLField()
    github = models.URLField()
    tech = models.JSONField()

    def __str__(self):
        return self.title
