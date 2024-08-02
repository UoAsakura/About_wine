from django.shortcuts import render
from django.http import (HttpResponse,
                         HttpResponseRedirect)
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .models import Feedback, ErrorMessage, InfoMessage
from .forms import FeedbackForm, ErrorMessageForm, InfoMessageForm
# Create your views here.


class DoneFeedback(ListView):
    template_name = "feedback/done_feedback.html"  # адрес html-шаблона внутри нашего приложения.
    model = Feedback  # Модель | БД из models.py откуда мы будем тянуть или класть информацию.
    # context_object_name = "feed"  # Имя, которое будет уходить в html-шаблон (по-умолч object_list).


class FeedbackView(FormView):
    form_class = FeedbackForm
    template_name = "feedback/submit_feedback.html"
    success_url = "/feedback/done"
    def form_valid(self, form):
        form.save()
        return super(FeedbackView, self).form_valid(form)


class ListFeedBack(ListView):
    template_name = "feedback/all_feedback.html"
    model = Feedback
    context_object_name = "context"
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class DetailFeedBack(DetailView):  # Наследуемся.
    template_name = 'feedback/detail_feedback.html'  # Обозначаем путь к html-файлу.
    model = Feedback  # Указываем в какой модели потребуется искать конкретный объект.
    context_object_name = "context"


class ErrorMessageView(CreateView):
    """
    Функция для обратной связи об ошибках от пользователей.
    """
    form_class = ErrorMessageForm
    template_name = "feedback/report_a_bug.html"
    success_url = "/feedback/done"
    model = ErrorMessage


class InfoMessageView(CreateView):
    """
    Функция для обратной связи об ошибках от пользователей.
    """
    form_class = InfoMessageForm
    template_name = "feedback/report_a_inaccuracy.html"
    success_url = "/feedback/done"
    model = InfoMessage
