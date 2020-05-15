# Generated by Django 3.0.5 on 2020-04-25 23:36

import Dog_Breed_Classifier.file_validator
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='uploads/%Y/%m/%d/', validators=[Dog_Breed_Classifier.file_validator.validate_file_extension])),
                ('category', models.CharField(default='Undefined', max_length=50)),
                ('processed', models.BooleanField(default=False)),
            ],
        ),
    ]
