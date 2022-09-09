from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    publishedAt = models.DateTimeField(auto_now_add = True)
    modifiedAt = models.DateTimeField(auto_now=True)
    activeYN = models.IntegerField(default=1)