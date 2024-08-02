from django.shortcuts import render, get_object_or_404
from django.http import (HttpResponseRedirect)
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView
from .models import Grape, Category, TagGrape
# from .forms import SelectCityForm


# cats_db = [
#     {'id': 'red', 'name': 'Красные'},
#     {'id': 'white', 'name': 'Белые'},
# ]


def presentation(request):
    """
    Функция главной страницы и приветствия пользователя.
    """
    return render(request, "grape_varieties/index.html")


def redirect_to_home_page(request):
    """
    Редирект на главную страницу.
    """
    redirect_url = reverse("total_page")
    return HttpResponseRedirect(redirect_url)


class ShowGrapes(ListView):
    template_name = "grape_varieties/about_grapes.html"  # адрес html-шаблона внутри нашего приложения.
    model = Grape  # Модель | БД из models.py откуда мы будем тянуть или класть информацию.
    # filter = "name_eng"
    ordering = "name_eng"
    context_object_name = "grapes"  # Имя, которое будет уходить в html-шаблон (по-умолч object_list).


class ShowOneGrape(DetailView):  # Наследуемся.
    template_name = 'grape_varieties/info_about_grape.html'  # Обозначаем путь к html-файлу.
    model = Grape  # Указываем в какой модели потребуется искать конкретный объект.


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    grapes = Grape.objects.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'grapes': grapes,
        'cat_selected': category.pk,
    }
    return render(request, "grape_varieties/about_grapes.html", context=data)


def show_tag_list(request, tag_slug):
    tag = get_object_or_404(TagGrape, slug=tag_slug)
    grapes = tag.tags.filter()
    data = {
        'title': f"Тег: {tag.tag}",
        'grapes': grapes,
        'cat_selected': None,
    }
    return render(request, "grape_varieties/about_grapes.html", context=data)


# def ShowHistory(request):
#     return render(request, "includes/for_history/about_history.html")

class ShowHistory(ListView):
    template_name = "includes/for_history/about_history.html"  # адрес html-шаблона внутри нашего приложения.
    model = Grape  # Модель | БД из models.py откуда мы будем тянуть или класть информацию.


# class FeedbackView(FormView):
#     form_class = SelectCityForm
#     template_name = "grape_varieties/about_grapes.html"
#     success_url = "grape_varieties/about_grapes.html"
#     def form_valid(self, form):
#         form.save()
#         return super(FeedbackView, self).form_valid(form)

