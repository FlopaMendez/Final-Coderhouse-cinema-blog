from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from usuarios import views

urlpatterns = [
    path("crear/", views.UserSignUp.as_view(), name ="user_signup"),
]