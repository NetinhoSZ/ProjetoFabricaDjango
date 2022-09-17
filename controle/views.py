from django.shortcuts import render, redirect
from .models import Mensalidade
from .forms import Mensalidadeform
import datetime

def home(request):
    data = {}

    data['now'] = datetime.datetime.now()
    data['mensalidades'] = Mensalidade.objects.all()
    return render(request, 'controle/home.html', data)

def listagem(request):
    data = {}
    data['mensalidades'] = Mensalidade.objects.all()
    return render(request, 'controle/listagem.html', data)

def nova_mensalidade(request):
    data = {}
    form = Mensalidadeform(request.POST or None)
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    
    return render(request, 'controle/form.html' , data)

def update(request, pk):
    data = {}
    mensalidade = Mensalidade.objects.get(pk=pk)
    form = Mensalidadeform(request.POST or None, instance=mensalidade)
    
    
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['mensalidade'] = mensalidade
    return render(request, 'controle/form.html', data) 

def delete(request, pk):
    mensalidade = Mensalidade.objects.get(pk=pk)
    mensalidade.delete() 
    return redirect('url_listagem') 

    
