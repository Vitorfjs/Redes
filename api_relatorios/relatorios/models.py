from django.db import models

class Relatorio(models.Model):
    titulo = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo

