from grape_varieties import views as views_grape
from django.urls import path

# Урлы с разделом о сортах винограда.
urlpatterns = [
    # Главная страница о сортах.
    path('', views_grape.ShowGrapes.as_view(), name="to_grapes"),
    path('<slug:slug>', views_grape.ShowOneGrape.as_view(), name='to_info_about_grapes'),
    path('category/<slug:cat_slug>', views_grape.show_category, name='category'),
    path('tag/<slug:tag_slug>', views_grape.show_tag_list, name='tag'),
    # path('tag/<slug:tag_slug>', views_grape.show_tag_grape, name='tag'),
]


# urlpatterns = [
# Главная страница о сортах.
    # path('', views_grape.all_grapes, name="to_all_grapes"),
    # path('', views_grape.white_grapes, name="to_white_grapes"),
    # path('', views_grape.red_grapes, name="to_red_grapes"),
    # path('', views_grape.autochthonous_grapes, name="to_autochthonous_grapes"),
    # path('', views_grape.international_grapes, name="to_international_grapesrequest"),
# ]