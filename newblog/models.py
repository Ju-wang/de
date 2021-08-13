from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", null=True, blank=True, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=100)

    def approve(self):
        self.save()
