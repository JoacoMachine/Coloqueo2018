# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import (Curso, Alumno)
from django.contrib import admin

# Register your models here.

admin.site.register(Curso)
admin.site.register(Alumno)