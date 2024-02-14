from django.db import models

class Diurese(models.Model):
    volume = models.CharField(max_length=10, blank=False, null=False)
    tempo = models.CharField(max_length=10, blank=False, null=False)


    def __str__(self):


        return self.volume

    class Meta:
        db_table = 'diurese'

    def to_dict(self):
        return {
            'value': self.pk,
            'volume': self.volume,
            'tempo': self.tempo
        }