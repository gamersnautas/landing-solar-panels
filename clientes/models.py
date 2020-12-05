from django.db import models

class Cliente(models.Model):
    name = models.CharField(verbose_name='Nombre del cliente', max_length=100, blank=False, null=False)
    email = models.CharField(verbose_name='Email del cliente', max_length=100, blank=False, null=False)
    phone = models.CharField(verbose_name='Telefono del cliente', max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

    