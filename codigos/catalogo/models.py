from django.db import models


class BiCard(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    url = models.CharField(max_length=400, null=False, blank=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'
