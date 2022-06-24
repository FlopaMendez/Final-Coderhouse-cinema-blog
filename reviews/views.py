
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from reviews.forms import BuscarPeliculaForm
from reviews.models import ReviewModel
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm



class ReviewsList(ListView):

    model = ReviewModel
    template_name = "reviews/reviews_list.html"


class ReviewsDetail(DetailView):

    model = ReviewModel
    template_name = "reviews/review_detail.html"


class ReviewCreate(LoginRequiredMixin, CreateView):

    model = ReviewModel
    success_url = reverse_lazy("reviews_list")
    fields = ["titulo", "director", "estreno", "cuerpo"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class ReviewUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = ReviewModel
    success_url = reverse_lazy("reviews_list")
    fields = ["titulo", "director", "estreno", "cuerpo"]

    def test_func(self):
        exist = ReviewModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False
        


class ReviewDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):

    model = ReviewModel
    success_url = reverse_lazy("reviews_list")

    def test_func(self):
        exist = ReviewModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False


def buscar_pelicula(request):
    if request.method == "GET":
        form_busqueda = BuscarPeliculaForm()
        return render(request, 'reviews/form_busqueda_.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarPeliculaForm(request.POST)
        if form_busqueda.is_valid():
            pelicula_a_buscar = form_busqueda.cleaned_data['pelicula_a_buscar']
            titulo = ReviewModel.objects.filter(titulo__icontains=pelicula_a_buscar)

        return  render(request, 'reviews/reviews_list.html', {"titulo": titulo})


def reviews_inicio(request):
    return render(request, 'reviews/reviews_inicio.html')

def about_us(request):
    return render(request, 'reviews/about_us.html')
    