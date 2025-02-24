from django.db import models

# Create your models here.

class New(models.Model):
    image = models.ImageField(upload_to='article/')
    title = models.CharField(max_length=221)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Worker(models.Model):
    title = models.CharField(max_length=221)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title