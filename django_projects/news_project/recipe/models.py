from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipe_images/')
    slug = models.SlugField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=1)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# class Recipe_Tag(models.Model):
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Ingredient(models.Model):
    UNIT_CHOICES = (
        (0, 'Kilogram'),
        (1, 'Gram'),
        (2, 'Litre'),
        (3, 'Piece'),
    )

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=200, decimal_places=2)
    unit = models.IntegerField(choices=UNIT_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

def recipe_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        if Recipe.objects.filter(slug=slugify(instance.title)).exclude(id=instance.id).exists():
            import uuid
            instance.slug = f"{slugify(instance.title)}-{str(uuid.uuid4()).split('-')[0]}"

pre_save.connect(recipe_pre_save, sender=Recipe)


# def ingredient_pre_save(sender, instance, *args, **kwargs):
#     if instance.slug is None:
#         if Ingredient.objects.filter(slug=slugify(instance.name)).exclude(id=instance.id).exists():
#             import uuid
#             instance.slug = f"{slugify(instance.name)}-{str(uuid.uuid4()).split('-')[0]}"

# pre_save.connect(ingredient_pre_save, sender=Ingredient)