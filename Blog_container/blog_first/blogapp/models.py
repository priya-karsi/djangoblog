from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    publishedAt = models.DateTimeField(auto_now_add = True)
    modifiedAt = models.DateTimeField(auto_now=True)
    activeYN = models.IntegerField(default=1)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

