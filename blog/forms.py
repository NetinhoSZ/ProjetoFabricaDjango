from django.forms import ModelForm 
from .models import Postagem 


class FormularioPostagem(ModelForm): 

    class Meta: 
        model = Postagem 
        fields = ['titulo', 'conteudo']
