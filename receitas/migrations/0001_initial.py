# Generated by Django 4.0.1 on 2022-01-10 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeReceita', models.CharField(max_length=200)),
                ('ingredientes', models.TextField()),
                ('modoPreparo', models.TextField()),
                ('tempoPreparo', models.IntegerField()),
                ('rendimento', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('dataReceita', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
