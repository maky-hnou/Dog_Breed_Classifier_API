# Generated by Django 3.0.5 on 2020-05-01 21:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dog_Breed_Classifier', '0003_auto_20200501_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='processing_time',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='upload_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
