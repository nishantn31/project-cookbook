from django.db import models
from django.contrib.auth.models import User
from .utils import generate_slug



class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.recipe_name)
        super(Recipe, self).save(*args, **kwargs)