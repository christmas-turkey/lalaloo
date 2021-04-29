from django.urls import path

from . import views

app_name = "videos"
urlpatterns = [
    path('', views.MainPage.as_view(), name="main-page"),
    path('videos/<uuid:video>', views.DetailVideo.as_view(), name="detail-video"),
    path('videos/<uuid:video>/comments/add', views.AddComment.as_view(), name="add-comment")
]