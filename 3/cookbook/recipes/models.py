from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"


class Recipe(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="receipes")
    prep_time = models.IntegerField() # in minutes

    def __str__(self):
        return f"{self.category}:{self.name}:{self.prep_time} min"


class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    recipe = models.ManyToManyField(Recipe, blank=True, related_name="ingredients")

    def __str__(self):
        return f"{self.name} - ${self.price}"
