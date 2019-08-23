from django.db import models
import datetime


class Music(models.Model):
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# True observations
class Target(models.Model):
    date = models.DateTimeField('episode_date')
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return f'Target, {self.date}: {self.predicted_music}'


class Prediction(models.Model):
    date = models.DateTimeField('episode date')
    entry_date = models.DateTimeField('entry_date', auto_now_add=True)
    method = models.CharField('prediction method', max_length=100)
    predicted_music = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return f'Prediction, {self.date}: {self.predicted_music} (by {self.method})'


class Vote(models.Model):
    date = models.DateTimeField('episode date')
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return f'Vote, {self.date}: {self.predicted_music}'