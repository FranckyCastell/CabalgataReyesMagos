from django.db import models
from django.utils import tree

# Create your models here.


class Cities (models.Model):
    name = models.CharField(verbose_name='Nom Poble',
                            max_length=50, blank=True, null=True)

    allName = models.CharField(verbose_name='Nom Complet Poble',
                               max_length=50, blank=True, null=True)

    descargar = models.FileField(
        verbose_name='PDF Ruta', blank=True, null=True)

    route = models.TextField(verbose_name='Ruta',
                             max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'ciutat'
        verbose_name_plural = 'ciutats'

    def __str__(self):
        return self.name


class Event (models.Model):
    citie = models.ForeignKey(
        Cities, verbose_name='Ciudad', null=True, blank=True, on_delete=models.CASCADE)

    title = models.CharField(verbose_name='Títol',
                             max_length=50, blank=True, null=True)

    start = models.CharField(verbose_name='Data Inici',
                             blank=True, null=True, default='2021-12-11T22:30:00', max_length=20)

    end = models.CharField(verbose_name='Data Final',
                           blank=True, null=True, default='2021-12-11T22:30:00', max_length=20)

    class Meta:
        verbose_name = 'esdeveniment'
        verbose_name_plural = 'esdeveniments'

    def __str__(self):
        return self.title
