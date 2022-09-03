from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    # date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
