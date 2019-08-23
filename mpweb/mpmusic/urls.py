from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^(?P<date>\d{4}-\d{2}-\d{2})/$', views.prediction, name='prediction')
]