from django.shortcuts import render
# import requests

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


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
context = {
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
    }
}
recipe_omlet = {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
}

recipe_pasta = {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
}

recipe_buter = {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
}

# def index(request):
#     return render(request, "calculator/index.html", context= context)

def index_omlet(request):
    count_recipe = request.GET.get('serving')
    if count_recipe and int(count_recipe)>1:
        recipe_omlet.update(
            (key, value * int(count_recipe)) for key, value in recipe_omlet.items()
        )
    return render(request, "calculator/index.html", context={'recipe':recipe_omlet})
def index_pasta(request):
    count_recipe = request.GET.get('serving')
    if count_recipe and int(count_recipe)>1:
        recipe_pasta.update(
            (key, value * float(count_recipe)) for key, value in recipe_pasta.items()
        )
    return render(request, "calculator/index.html", context={'recipe':recipe_pasta})

def index_buter(request):

    count_recipe = request.GET.get('serving')
    if count_recipe and int(count_recipe)>1:
        recipe_buter.update(
            (key, value * int(count_recipe)) for key, value in recipe_buter.items()
        )
    return render(request, "calculator/index.html", context={'recipe':recipe_buter})