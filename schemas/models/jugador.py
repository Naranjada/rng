# -*- coding: utf-8 -*-
from django.db import models
from schemas.models.team import Team


class Jugador(models.Model):
	name = models.CharField(max_length=255,verbose_name="jugador")
	team = models.ForeignKey(Team,verbose_name='equipo',blank=True,null=True)
	country = models.CharField(max_length=155,verbose_name='nacionalidad')
	goals = models.IntegerField(verbose_name='cantidad de goles',default=0)

	def __unicode__ (self,):
		return "[%s] %s %s %s" % (self.goals, self.name, self.team, self.country)
		

	class Meta:
		verbose_name = "jugador"
		verbose_name_plural	= "jugadores"
		ordering = ['-goals']