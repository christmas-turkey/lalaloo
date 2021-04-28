from django.urls import path, include

from . import views

app_name = "account"
urlpatterns = [
  path('signin/', views.SignIn.as_view(), name="signin"),
  path('signup/', views.SignUp.as_view(), name="signup"),
  path('signout/', views.SignOut.as_view(), name="signout"),
  path('<str:username>/', views.Profile.as_view(), name="profile")
]