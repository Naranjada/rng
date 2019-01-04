from django.core.management.base import BaseCommand
from schemas.models.team import Team

class ScriptRun(object):

    def __init__(self):
        pass

    def do(self):
        teams = ['Chelsea', 'ManchesterUnited', 'RealMadrid', 'Barcelona', 'InterdeMilan', 'Roma', 'Liverpool', 'Arsenal', 'BayernMunich', 'Juventus', 'England', 'Francia', 'Argentina', 'Brasil', 'Espania', 'Holanda', 'PSG', 'Dortmund', 'Belgica', 'Portugal', 'Uruguay', 'Tottenham', 'AtleticoMadrid', 'Napoli', 'ManchesterCity', 'Milan', 'Italia', 'Alemania', 'Croacia', 'ComodinA', 'Monaco', 'Polonia', 'Suiza', 'Everton', 'Chile', 'Villareal', 'Rusia', 'Leicester', 'Porto', 'Colombia', 'Ajax', 'Mexico', 'Sevilla', 'CrystalPalace', 'Turkey', 'Marseille', 'Benfica', 'Lazio', 'Lyon', 'SportingLisboa', 'Brujas', 'Leverkusen' , 'Serbia', 'WestHam', 'Dinamarca', 'Zenith', 'FCShalke04', 'Leipzig', 'Valencia', 'River', 'Boca']
        for team in teams:
        	print team
        	Team.objects.create(name=team)

class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()

    def handle(self, *args, **options):
        run = ScriptRun()
        run.do()