# Generated by Django 4.1.7 on 2023-02-19 03:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern', models.FileField(upload_to='pdfs/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('pattern_name', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('date_added', models.DateField()),
                ('is_embroidery', models.BooleanField()),
                ('is_cross_stitch', models.BooleanField()),
            ],
        ),
    ]
