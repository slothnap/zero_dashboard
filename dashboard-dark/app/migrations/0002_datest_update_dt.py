# Generated by Django 3.2.11 on 2022-02-16 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datest',
            name='update_Dt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
