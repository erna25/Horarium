from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    telephone = models.CharField(max_length=12)

    def __str__(self):
        return self.title


class CategoryTicket(models.Model):
    title = models.CharField("Категория", max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Ticket(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь",
                             on_delete=models.CASCADE)
    title = models.CharField("Тема тикета", max_length=100)
    body = models.TextField("Текст тикета", max_length=1000)


class Meta:
    verbose_name = "Тикет"
    verbose_name_plural = "Тикеты"


def __str__(self):
    return "{}{}".format(self.title, self.user)
# Create your models here.
