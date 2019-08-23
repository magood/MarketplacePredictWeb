from django.core.management.base import BaseCommand, CommandError
from mpmusic.models import Prediction, Music
import subprocess
from datetime import datetime, timedelta
from django.utils.timezone import make_aware


class Command(BaseCommand):
    help = 'Runs prediction routine, imports/stores result'

    def add_arguments(self, parser):
        parser.add_argument('daysago', nargs='?', default=0, type=int)

    def handle(self, *args, **options):
        daysago = options["daysago"]
        predpath = r'C:\Users\Matthew\Documents\Development\MarketplacePredict\Predict\MarketplacePredict\pred.txt'
        music_prediction = None
        with open(predpath, 'r') as file:
            music_prediction = file.read().strip()
        if music_prediction is None:
            self.stdout.write('Could not retrieve prediction, exiting.')
        else:
            mp = Music.objects.filter(code=music_prediction).first()
            prediction_day = datetime.today() - timedelta(days=daysago)
            aware_pday = make_aware(prediction_day)
            pred = Prediction.objects.filter(
                date__year=aware_pday.year,
                date__month=aware_pday.month,
                date__day=aware_pday.day)
            if pred:
                self.stdout.write("deleting existing prediction")
                pred.delete()
            pred = Prediction(date=aware_pday, method='SVM', predicted_music=mp)
            pred.save()
            self.stdout.write(self.style.SUCCESS('Successfully imported prediction'))