from django.db import models


class Faculty(models.Model):
    id_F = models.IntegerField()
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Group(models.Model):
    id_G = models.IntegerField()
    id_F = models.IntegerField()
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Subject(models.Model):
    id_S = models.IntegerField()
    id_G = models.IntegerField()
    title = models.CharField(max_length=120)
    teacher = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    id_L = models.IntegerField()
    id_S = models.IntegerField()
    cabinet = models.CharField(max_length=10)
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return self.title
# Create your models here.
