from django.db import models

class Videos(models.Model):
  nome_video = models.CharField(max_length=255)
  descricao_video = models.CharField(max_length=255)
  joined_date = models.DateField(null=True)
  uri = models.DateField(null=True)
  def __str__(self):
    return f"{self.firstname} {self.lastname}"
  