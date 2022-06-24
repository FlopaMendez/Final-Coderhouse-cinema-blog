# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path
from usuarios import views

urlpatterns = [
    path("crear/", views.UserSignUp.as_view(), name ="user_signup"),
    path("profile/<pk>/", views.UserProfile.as_view(), name ="user_profile"),
    path("editar/<pk>/", views.UserUpdate.as_view(), name ="profile_edit"),
    path("entrar/", views.UserLogin.as_view(), name="user_login"),
    path("salir/", views.UserLogout.as_view(), name="user_logout"),
]