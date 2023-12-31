from django.shortcuts import render
from django.shortcuts import get_object_or_404  
from .models import Produto
from django.http import HttpResponse
from django.template import loader
#É aquele que faz ter as funções que serão chamadas nas nossas rotas para então, abrir os templates para ser visualizadas.
from .models import Produto
def index(request):
    produtos=Produto.objects.all()
    context={
        'curso': 'PROGRAMAÇÃO COM O FRAMEWORK DJANGO',
        'outro': 'Django é massa',
        'produtos':produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request,'contato.html')
def produto(request,pk):
    #prod=Produto.objects.get(id=pk)
    prod=get_object_or_404(Produto, id=pk)
    context={
        'produto': prod
    }
    return render(request, 'produto.html',context)

def error404(request, ex):
    tamplate=loader.get_template('404.html')
    return HttpResponse(content=tamplate.render(), content_type='text/html;charset= utf8', status=404)
def error500(request):
    tamplate=loader.get_template('500.html')
    return HttpResponse(content=tamplate.render(), content_type='text/html;charset= utf8', status=500)