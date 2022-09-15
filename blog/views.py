from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def alecrim(request):
    
    return render(request, template_name= 'blog/home.html')
    
def dourado(request):
    html = "<html><body><h1>Dourado!</h1></body></html>"
    return HttpResponse(html)
