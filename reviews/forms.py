from django import forms

class BuscarPeliculaForm(forms.Form):
    pelicula_a_buscar = forms.CharField(label="Buscar")