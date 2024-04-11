from django.db import models


class Human(models.Model):
    name = models.CharField('Name:', max_length=30)
    age = models.IntegerField('Age:')
    date_of_burn = models.DateField('Date of burning:')
