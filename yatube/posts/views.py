from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = "posts/index.html"
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = "Yatube"
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        "title": title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        "text": "Это главная страница проекта Yatube",
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


# Страница со списком мороженого
def posts_list(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = "posts/group_list.html"
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = "Группы"
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        "title": title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        "text": "Здесь будет информация о группах проекта Yatube",
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def group_posts(request, pk):
    return HttpResponse(f"Посты в группе {pk}")
