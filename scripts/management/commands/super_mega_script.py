from django.core.management.base import BaseCommand
from schemas.models.team import Team
from schemas.models.jugador import Jugador
import os, json
import ast

class ScriptRun(object):

    def __init__(self):
        pass

    def do(self):
        
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        db = open( BASE_DIR + '/commands/db.txt', 'r')
        lista = []

        for line in db.readlines():
            line = line.replace('\n', '')

            line = line.split(',')


            lista.append(
                {
                'player': line[0],
                'team': line[1],
                'country': line[2]
                }
            )


        for a in lista:
            try:
                team = Team.objects.create(
                    name=a['team']
                )

                team.save()
            except Exception as e:
                team = Team.objects.get(name=a['team'])


            jugador = Jugador.objects.create(
                name=a['player'],
                team=team,
                country=a['country']
            )
            
            jugador.save()

            print a


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()

    def handle(self, *args, **options):
        run = ScriptRun()
        run.do()

