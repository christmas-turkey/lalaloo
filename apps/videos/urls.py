from django.urls import path

from . import views


app_name = "videos"
urlpatterns = [
    path('', views.MainPage.as_view(), name="main-page"),
    path('privacy-policy/', views.PrivacyPolicy.as_view(), name="privacy-policy"),
    path('videos/<uuid:video>', views.DetailVideo.as_view(), name="detail-video"),
    path('videos/<uuid:video>/like', views.LikeVideo.as_view(), name="like-video"),
    path('videos/<uuid:video>/comments/add', views.AddComment.as_view(), name="add-comment")
]