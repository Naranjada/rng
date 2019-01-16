from django.shortcuts import render
from schemas.models.team import Team
from schemas.models.jugador import Jugador
from django.views.generic import ListView
from django.http import HttpResponseRedirect

class TableListView(ListView):
	model = Jugador
	context_object_name = "jugadores"
	template_name = "table.html"

	def post(self, request):
		form = request.POST
		jugador = Jugador.objects.get(id=form.get('playerid'))
		jugador.goals = jugador.goals+int(form.get('goals'))
		jugador.save()
		return HttpResponseRedirect("/table")
