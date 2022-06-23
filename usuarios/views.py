from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView


class UserSignUp(SuccessMessageMixin, CreateView):
  template_name = 'usuarios/crear_user_form.html'
  success_url = reverse_lazy('user_login')
  form_class = UserCreationForm
#   success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"


class UserLogin(LoginView):
    template_name = 'usuarios/user_login.html'
    next_page = reverse_lazy("reviews_list")


class UserLogout(LogoutView):
    template_name = 'usuarios/user_logout.html'


