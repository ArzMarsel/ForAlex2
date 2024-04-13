from django.db import models
from django.core.validators import MaxLengthValidator


class Human(models.Model):
    name = models.CharField('Name:', max_length=30, validators=[MaxLengthValidator(10)])
    age = models.IntegerField('Age:')
    date_of_burn = models.DateField('Date of burning:')
