from django.core.management.base import BaseCommand

class ScriptRun(object):

    def __init__(self):
        pass

    def do(self):
        print "Mira mama estoy corriendo"

class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()

    def handle(self, *args, **options):
        run = ScriptRun()
        run.do()