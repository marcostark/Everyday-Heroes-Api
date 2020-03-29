from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    # Usar email como login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class CollectPoint(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile_client')
    description = models.CharField(verbose_name='Descrição', max_length=255)
    itens = models.CharField(verbose_name='Itens para Doação', max_length=255)
    people_quantity = models.IntegerField(verbose_name='Quantidade de Pessoas')
    city = models.CharField(verbose_name='Cidade', max_length=255)
    neighborhood = models.CharField(verbose_name='Bairro', max_length=500)
    street = models.CharField(verbose_name='Rua', max_length=500)
    street_number = models.IntegerField(verbose_name='Número')
    cep = models.CharField(verbose_name='CEP', max_length=9, blank=True, null=True)

    def __str__(self):
        return self.city
