from django import forms
from feedback.models import (Feedback,
                             ErrorMessage,
                             InfoMessage,)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
        # exclude = ["", ""]
        labels = {
            "name": "Имя",
            "feedback": "Отзыв",
            "rating": "Рейтинг",
        }


class ErrorMessageForm(forms.ModelForm):
    class Meta:
        model = ErrorMessage
        fields = "__all__"
        labels = {
            "name": "Имя",
            "type_error": "Тип ошибки",
            "about_error": "Информация об ошибке",
            "image": "Изображение",
        }


class InfoMessageForm(forms.ModelForm):
    class Meta:
        model = InfoMessage
        fields = "__all__"
        labels = {
            "name": "Имя",
            "type_inaccuracy": "Тип неточности",
            "about_inaccuracy": "Информация о неточности",
            "image": "Изображение",
        }



# class FeedbackForm(forms.Form):
#     name = forms.CharField(label="Имя",
#                            min_length=2,
#                            max_length=8,
#                            error_messages={
#                                "min_length":"Слишком мало символов",
#                                "max_length": "Слишком много символов",
#                                "required": "Укажите хотя бы пару символов",
#                            })
#     surname = forms.CharField(label="Фамилия")
#     rating = forms.IntegerField(label="Рейтинг",
#                                 min_value=1,
#                                 max_value=5)
#
#     feedback = forms.CharField(label="Отзыв",
#                                widget=forms.Textarea)


# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         fields = "__all__"
#         labels = {
#             "name": "Имя",
#             "surname": "Фамилия",
#             "feedback": "Отзыв",
#             "rating": "Рейтинг",
#         }
#         error_messages = {
#             "name": {
#                 "min_length": "Слишком мало символов",
#                 "max_length": "Слишком много символов",
#                 "required": "Укажите хотя бы пару символов",
#             }
#         }