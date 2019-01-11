# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from schemas.models.team import Team
from schemas.models.jugador import Jugador


class JugadorAdmin(admin.ModelAdmin):
	list_display = ("name", "team", "goals", "country",)
	search_fields = ("name","team__name",)
	list_filter = ("team",)
	ordering = ("goals",)
admin.site.register(Jugador, JugadorAdmin)

class TeamAdmin(admin.ModelAdmin):
	list_display = ("name",)
	ordering = ("name",)
admin.site.register(Team, TeamAdmin)