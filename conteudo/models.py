

from email.policy import default
from django.db import models

from django.contrib.auth.models import User






class Pais(models.Model):
    nome_pais = models.CharField(
        max_length=28,
        null=False,
        blank=False
    )
    lingua_oficial = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    continente = models.CharField(
        max_length=35,
        null=False,
        blank=False
    )
    clima = models.TextField(
        blank=False,
        null=False,
        default="A nice country"
    )
    descricao = models.TextField(
        blank=False,
        null=False,
        default="A nice country"
    )

    objetos = models.Manager()

    def __str__(self):
        return self.nome_pais



class Universidade(models.Model):
    nome_universidade = models.CharField(
        max_length=255,
        null=False,
        blank=False
        )
    historia = models.TextField(blank=True)

    localizacao_pais = models.ForeignKey(
        'Pais',
        on_delete=models.DO_NOTHING
    )

    localizacao_cidade = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )

    cultura = models.TextField(
        null=True,
        blank=True

    )

    taxa_aceitacao = models.DecimalField(
        max_digits=4, 
        decimal_places=2,
        null=True,
        blank=True
    )

  

    oferece_bolsa = models.BooleanField()

    descricao_bolsa = models.TextField()

    descricao_application = models.TextField()



   

    objetos = models.Manager()

    def __str__(self):
        return self.nome_universidade

class CollegeList(models.Model):
    universidade_desejada = models.ForeignKey(
        'Universidade',
        on_delete=models.CASCADE
    )

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null= True,
        blank= True

     
    )

class ListaNews(models.Model):
    email_news = models.CharField(
        max_length=255,
        null=False,
        blank=False
    ) 

    def __str__(self):
        return self.email_news 


    

   