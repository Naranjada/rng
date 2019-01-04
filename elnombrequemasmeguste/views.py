# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from schemas.models.team import Team
import random

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        equipos = (random.sample(set(Team.objects.all()), 12))

        lista = [
            {'player': "Alan 'The Legend' Sanchez ", 'equipo1': equipos[0], 'equipo2': equipos[1], 'equipo3': equipos[2], 'equipo4': equipos[3] },
            {'player': "Sebastian 'Cepita' Nodari", 'equipo1': equipos[4], 'equipo2': equipos[5], 'equipo3': equipos[6], 'equipo4': equipos[7] },
            {'player': "Agustin 'Pato' Rodriguez", 'equipo1': equipos[8], 'equipo2': equipos[9], 'equipo3': equipos[10], 'equipo4': equipos[11] },
        ]
        print lista
        context['lista'] = lista
        return context

