from grape_varieties import views as views_grape
from django.urls import path

# Урлы с разделом о истории виноделия.
urlpatterns = [
    # Главная страница о историях.
    path('', views_grape.ShowHistory.as_view(), name="to_history"),
    # path('<slug:slug>', views_grape.ShowOneGrape.as_view(), name='to_info_about_history'),
    # path('category/<slug:cat_slug>', views_grape.show_category, name='history_category'),
    # path('tag/<slug:tag_slug>', views_grape.show_tag_list, name='history_tag'),
]