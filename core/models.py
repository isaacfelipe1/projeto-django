#models é onde criamos os modelos de dados, ou seja, as nossas classes, aquilo que a gente vai persitir dentro do banco de dados de alguma forma, ou, utilizar no nosso projeto.
from django.db import models

class Produto(models.Model):
    nome=models.CharField('Nome', max_length=100)
    preco=models.DecimalField('Preço',decimal_places=2, max_digits=8)
    estoque=models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return f'{self.nome}'

class Cliente(models.Model):
    nome=models.CharField('Nome', max_length=100)
    sobrenome=models.CharField('Sobrenome', max_length=100)
    email=models.EmailField('E-mail',max_length=100)
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'




