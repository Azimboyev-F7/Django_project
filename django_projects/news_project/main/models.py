from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save



# Create your models here.

class New(models.Model):
    image = models.ImageField(upload_to='article/')
    title = models.CharField(max_length=221)
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

class Login(models.Model):
    username = models.CharField(max_length=221)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


    # def article_pre_save(sender, instance, *args, **kwargs):
    #     if instance.slug is None:
    #         instance.slug = slugify(instance.title)
    #     print("before saving")


    def article_pre_save(sender, instance, *args, **kwargs):
        instance.slug = slugify(instance.title)
        if New.objects.filter(slug=slugify(instance.title)).exclude(id=instance.id).exists():
            import random
            import uuid
            instance.slug += f"-{str(uuid.uuid4()).split('-')[0]}"
            # instance.slug += f"-{random.randint(1000, 9999)}"
    # def article_post_save(sender, instance, *args, **kwargs):


    pre_save.connect(article_pre_save, sender=New)
    # post_save.connect(article_post_save, sender=New)