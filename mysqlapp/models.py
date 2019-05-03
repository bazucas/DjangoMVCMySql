from django.db import models

class Questao(models.Model):
    questao_texto = models.CharField(max_length=200)
    data_pub = models.DateTimeField('data publicacao')
    def __str__(self):
        return self.questao_texto

class Opcao(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    opcao_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return self.opcao_texto

class Participante(models.Model):
    opcao = models.ForeignKey(Opcao, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.nome