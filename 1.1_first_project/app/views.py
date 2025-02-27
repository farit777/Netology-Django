from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': '',
        'Показать содержимое рабочей директории': ''
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # Получаем текущее время
    now = datetime.now()
    # Форматируем текущее время как строку
    time_str = now.strftime('%Y-%m-%d %H:%M:%S')
    # Возвращаем ответ с текущим временем
    return HttpResponse(f'Текущее время: {time_str}')


def workdir_view(request):
    # Получаем текущую рабочую директорию
    current_dir = os.getcwd()
    # Получаем список файлов и директорий в текущей директории
    items = os.listdir(current_dir)
    # Форматируем список в строку для вывода
    items_str = "<br>".join(items)  # Преобразуем в HTML-формат (построчно)
    # Возвращаем ответ с содержимым рабочей директории
    return HttpResponse(f'Текущая рабочая директория: {current_dir}<br>Содержимое:<br>{items_str}')
