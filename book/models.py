from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Ingredients(models.Model):
    title = models.CharField(max_length=80, verbose_name='Ingredients', default=None)
    amount = models.IntegerField(verbose_name='Amount')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'


class Recipe(models.Model):
    COMPLEXITY_CHOICES = [
        (5, 5),
        (4, 4),
        (3, 3),
        (2, 2),
        (1, 1)
    ]

    title = models.CharField(max_length=80, verbose_name='Recipe name')
    ingredients = models.ManyToManyField(Ingredients, related_name='Ingredients')
    cooking_time = models.IntegerField(verbose_name='Cooking time')
    cooking_method = models.TextField(verbose_name='Cooking method')
    slug = models.SlugField(unique=True)
    complexity = models.IntegerField(choices=COMPLEXITY_CHOICES, verbose_name='Complexity', default=1)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    def get_absolute_url(self):
        return reverse("recipe_info", kwargs={"recipe_slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
