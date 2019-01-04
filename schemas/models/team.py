from django.db import models

class Team(models.Model):
	name = models.CharField(max_length=100,verbose_name="equipo")

	def __str__ (self):
		return self.name

	class Meta:
		verbose_name = "equipo"
		verbose_name_plural	= "equipos"