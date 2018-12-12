# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from asistencia.models import Curso
# Create your views here.
def asistecia_render(request):
    context = {}
    context['Curso'] = Asistencia.objects.all().order_by('-datetime')
    return render(request, 'asistencia/index.html', context)