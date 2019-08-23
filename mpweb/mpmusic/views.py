from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import datetime

from .models import Prediction


def index(request):
    # TODO redirect
    return HttpResponse(f"Hello, world. You're at the index.")


def prediction(request, date=timezone.now()):
    date_format = '%Y-%m-%d'
    unaware_start_date = datetime.datetime.strptime(date, date_format)
    date_to_use = unaware_start_date or timezone.localtime(timezone.now()).date()
    pred = Prediction.objects.filter(
        date__year=date_to_use.year,
        date__month=date_to_use.month,
        date__day=date_to_use.day)
    context = {'prediction': pred.first()}
    return render(request, 'mpmusic/prediction.html', context)