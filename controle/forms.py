from django.forms import ModelForm 
from .models import Mensalidade 

class Mensalidadeform(ModelForm):
    class Meta:
        model = Mensalidade 
        fields = ['aluno', 'valor', 'plano', 'treino']