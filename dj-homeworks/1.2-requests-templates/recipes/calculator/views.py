from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

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
    # можете добавить свои рецепты ;)
}

def recipe(request, recipe_name):
    if recipe_name in DATA:
        data = DATA[recipe_name]
        servings = request.GET.get('servings', None)

        if servings:
            var = dict()
            for item, value in data.items():
                new_value = value * int(servings)
                var[item] = new_value
            context = {
                'recipe': data,
                'recipe_name': recipe_name
            }
        else:
            context = {
                'recipe_name': recipe_name,
                'recipe': data
            }
    else:
        context = None

    return render(request, template_name='calculator/index.html', context = context)


def home_view(request):

    recipe = list(DATA.keys())
    context = {'recipes': recipe}

    return render(request, template_name='calculator/home.html', context = context)
