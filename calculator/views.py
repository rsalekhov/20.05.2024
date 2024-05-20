from django.http import HttpResponse
from django.shortcuts import render

# Словарь с рецептами и их ингредиентами
DATA = {
    'omlet': {'яйца': 2, 'молоко': 0.1, 'соль': 0.5},
    'pasta': {'макароны': 200, 'сыр': 100, 'масло': 30},
    # Другие рецепты здесь
}

def recipe_view(request, dish):
    servings = int(request.GET.get('servings', 1))  # Количество порций
    recipe = DATA.get(dish, {})  # Получение рецепта
    scaled_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}
    context = {'recipe': scaled_recipe}
    return render(request, 'recipe.html', context)
