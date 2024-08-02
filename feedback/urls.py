from feedback import views as views_feedback
from django.urls import path


urlpatterns = [
    path('', views_feedback.FeedbackView.as_view()),
    path('done', views_feedback.DoneFeedback.as_view()),
    path('all_feedbacks', views_feedback.ListFeedBack.as_view(), name="all_feed"),
    path('detail/<int:pk>', views_feedback.DetailFeedBack.as_view(), name="one_feedback"),
    path('report_a_bug', views_feedback.ErrorMessageView.as_view()),
    path('report_a_inaccuracy', views_feedback.InfoMessageView.as_view()),
    # path('', views_feedback.hello),
]