from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Recipe, Ingredient, Category


# Create your views here.
def index(request):
    context = {
        "recipes": Recipe.objects.all()
    }
    return render(request, "recipes/index.html", context)


def recipe(request, recipe_id):
    i = 0

    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    context = {
        "recipe": recipe,
        "ingredients": recipe.ingredients.all(),
        "non_ingredients": Ingredient.objects.exclude(recipe=recipe).all()
    }
    return render(request, "recipes/recipe.html", context)


def add(request, recipe_id):
    try:
        ingredient_id = int(request.POST["ingredient"])
        recipe = Recipe.objects.get(pk=recipe_id)
        ingredient = Ingredient.objects.get(pk=ingredient_id)
    except KeyError:
        return render(request, "recipes/error.html", {"message": "No selection."})
    except Recipe.DoesNotExist:
        return render(request, "recipes/error.html", {"message": "No recipe."})
    except Ingredient.DoesNotExist:
        return render(request, "recipes/error.html", {"message": "No ingredient."})

    # associate with recipe
    ingredient.recipe.add(recipe)

    # recipe.ingredients.add(recipe)

    return HttpResponseRedirect(reverse("recipe", args=(recipe_id,)))
