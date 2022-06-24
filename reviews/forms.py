from django import forms

class BuscarPeliculaForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")