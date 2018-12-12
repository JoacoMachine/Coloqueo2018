# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.
class Curso(models.Model):
    message = models.CharField('Texto', max_length=142)
    datetime = models.DateTimeField('Fecha',auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuario")
    archived = models.BooleanField(default=False)
    
class Alumno(models.Model):
    message = models.CharField('Texto', max_length=142)
    datetime = models.DateTimeField('Fecha',auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuario")
    archived = models.BooleanField(default=False)
    
    def __str__(self):
        return 'Asistencia nro {} - by {}'.format(self.id, self.user)
    
    def __str__(self):
        return 'Alumno nro {} - by {}'.format(self.id, self.user)