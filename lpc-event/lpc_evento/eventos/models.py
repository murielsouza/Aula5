from django.db import models
from django.contrib.auth.models import User

class Endereco(models.Model):
    logradouro = models.CharField(max_length=128)
    complemento = models.CharField(max_length=256, null=True)
    uf = models.CharField(max_length=2, null=True)
    cidade = models.CharField(max_length=64, null=True)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return '{} - {}, {}'.format(self.logradouro, self.cidade, self.uf)
class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, related_name="pessoas", null=True, blank=False, on_delete=models.CASCADE)
    #usuario = models.OneToOneField(User)

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=15)
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)

    def __str__(self):
        return self.cpf

class Evento(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    sigla = models.CharField(max_length=14)
    logo = models.CharField(max_length=40)
    ano = models.IntegerField(max_length=4)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, related_name="eventos", null=True, blank=False, on_delete=models.CASCADE)
    realizador = models.ForeignKey(PessoaFisica, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Inscricao(models.Model):
    participante = models.ForeignKey(PessoaFisica, related_name="inscrições", null=True, blank=False, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, related_name="inscrições", null=True, blank=False, on_delete=models.CASCADE)
    data_inscricao = models.DateTimeField(blank=True, null=True)
    preco = models.FloatField()
