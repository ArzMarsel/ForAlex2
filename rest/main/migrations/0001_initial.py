# Generated by Django 5.0.4 on 2024-04-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name:')),
                ('age', models.IntegerField(verbose_name='Age:')),
                ('date_of_burn', models.DateField(verbose_name='Date of burning:')),
            ],
        ),
    ]
