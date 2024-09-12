from django.db import models
from datetime import date

# Create your models here.
class To_do(
    models.Model
):  # toda classe model precisa ter o model passado coomo parametro / toda classe é uma tabela do banco de dados
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de entrega", null=False, blank=False)
    finished_at = models.DateField(null=True)

    class Meta:
        ordering = ["deadline"] #responsavel por ordenar os objetos pela data de deadline

    def mark_has_complete(self): #resposavel por verificar se o finished at ja esta preenchido se nao ele completa com a data atua e att no banco
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()
