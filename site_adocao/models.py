
from django.db import models

class Apoio(models.Model):
    nome = models.CharField(max_length=50)
    contato = models.CharField(max_length=11, default="")
    logo = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.nome

class Cachorro(models.Model):

    numero_chip = models.IntegerField(max_length=6)
    nome = models.CharField(max_length=30)
    raca = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1)
    idade = models.IntegerField(max_length=4)
    cor = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    foto1 = models.ImageField(upload_to='media', blank=True)
    foto2 = models.ImageField(upload_to='media', blank=True)
    foto3 = models.ImageField(upload_to='media', blank=True)


    def __str__(self):
        return self.nome

class Gato(models.Model):


    numero_chip = models.IntegerField(max_length=6)
    nome = models.CharField(max_length=30)
    raca = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1)
    idade = models.IntegerField(max_length=4)
    cor = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    foto1 = models.ImageField(upload_to='media', blank=True)
    foto2 = models.ImageField(upload_to='media', blank=True)
    foto3 = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.nome

class Outro(models.Model):

    numero_chip = models.IntegerField(max_length=6)
    nome = models.CharField(max_length=30)
    raca = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1)
    idade = models.IntegerField(max_length=4)
    cor = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    foto1 = models.ImageField(upload_to='media', blank=True)
    foto2 = models.ImageField(upload_to='media', blank=True)
    foto3 = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.nome

