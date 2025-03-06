from django.http import HttpResponse
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def home_view(request):
    template_name = 'calculator/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def recipe_view(request, recipe_name):
    template_name = 'calculator/index.html'

    # Получаем servings из GET параметров, если он не указан, устанавливаем значение по умолчанию
    servings = request.GET.get('servings', 1)

    try:
        # Пробуем конвертировать servings в число
        servings = int(servings)
    except ValueError:
        # В случае ошибки конвертации, устанавливаем значение по умолчанию
        servings = 1

    # Получаем рецепт из DATA по имени
    recipe = DATA.get(recipe_name)

    # if recipe is None:
    #     # Если рецепт не найден, можно вернуть ошибку 404 или другой обработчик
    #     return render(request, 'calculator/404.html')

    # Умножаем количество каждого ингредиента на servings
    ingredients = {ingredient: quantity * servings for ingredient, quantity in recipe.items()}

    # Формируем контекст
    context = {
        'recipe': ingredients
    }

    # Возвращаем рендеринг шаблона с контекстом
    return render(request, template_name, context)
