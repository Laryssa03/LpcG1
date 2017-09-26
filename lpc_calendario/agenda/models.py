from django.db import models
from django.contrib.auth.models import User
from django import forms

class Agenda(models.Model):
    nome = models.CharField(max_length=128)
    usuario = models.ForeignKey(User)

    TIPO_CHOICES = (
        ('Publica', 'Pública'),
        ('Privada', 'Privada'),
        ('Institucional','Institucional')
    )
    tipo = models.CharField(max_length=14, choices=TIPO_CHOICES, blank=False, null=False)



    def __str__(self):
        return self.nome

class Convidar(models.Model):
    afitriao=models.ForeignKey(User)
    convidado=models.ForeignKey(User)
    confimar=models.BooleanField(default=1)
    
    def __str(self):
        return bool(self.confimar)


class Compromisso(models.Model):
    nome = models.CharField(max_length=128)
    dataHora = models.DateTimeField(blank=True, null=True)
    local = models.CharField(max_length=60)
    notas = models.TextField()
    agenda = models.ForeignKey(Agenda, null=True, blank=False) 
    convidar= models.ForeingnKey(Convidar,)
    def __str__(self):
        return self.nome + "( " + self.agenda.nome + " )"



