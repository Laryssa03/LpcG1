from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import *


def todasAgendas(request):
    retorno = "<h1> TODAS AGENDAS CADASTRADAS </h1>"
    listaAgendas = Agenda.objects.all()
    for a in listaAgendas:
        retorno += '<br> Nome Agenda: {} <br> Agenda criada por: {} <br> Tipo Agenda: {} <br> <br> '.format(a.nome, a.usuario.username, a.tipo)
    return HttpResponse(retorno)

def get_userAgendas_byID(request, id):
    retorno = "<h1> AGENDAS PÚBLICAS DE FULANINHO </h1>"
    listaAgendasPublicas = Agenda.objects.filter(tipo='Publica',usuario__id=id)
    for a in listaAgendasPublicas:
        retorno += '<br> Nome Agenda: {} <br> <br> '.format(a.nome)
    return HttpResponse(retorno)

def agendaInstitucional(request):
    retorno = "<h1> TODOS OS COMPROMISSOS INSTITUCIONAIS </h1>"
    listaCompromissosInstitucionais = Compromisso.objects.filter(agenda__tipo='Institucional')
    for c in listaCompromissosInstitucionais:
        retorno += '<br> Nome Compromisso: {} <br> <br> '.format(c.nome)
    return HttpResponse(retorno)


# Create your views here.
#a = AgendaPublica.objects.get(pk=id)
