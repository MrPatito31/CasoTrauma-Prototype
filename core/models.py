from django.db import models

class Emergencia(models.Model):
    id_emergencia = models.AutoField(primary_key=True)
    numero_paciente = models.IntegerField()
    contexto_emergencia = models.CharField(max_length=200)