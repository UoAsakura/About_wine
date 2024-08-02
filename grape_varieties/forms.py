from django import forms
from grape_varieties.models import Grape


# class SelectCityForm(forms.Form):
#     CITY_1 = 'city_1'
#     CITY_2 = 'city_2'
#     CITY_CHOICES = (
#         (CITY_1, u"City 1"),
#         (CITY_2, u"City 2")
#     )
#     cities = forms.ChoiceField(choices=CITY_CHOICES)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Grape
        fields = "__all__"
        # exclude = ["", ""]
        labels = {
            "name_eng": "Название сорта на английском",
            "color": "Цвет",
            "area": "Площаль посадок",
            "image": "Изображение сорта",
            "about_grape": "Информация о сорте",
        }
