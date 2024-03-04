from django.db import models


# Create your models here.
class ProjectItem(models.Model):
    title = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=200)
    description = models.TextField()
