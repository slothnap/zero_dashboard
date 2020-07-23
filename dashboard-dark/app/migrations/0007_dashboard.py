# Generated by Django 2.1.15 on 2020-07-23 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0006_delete_dashboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('no', models.IntegerField(blank=True, null=True)),
                ('dvsn', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('day1', models.IntegerField(blank=True, null=True)),
                ('day2', models.IntegerField(blank=True, null=True)),
                ('day3', models.IntegerField(blank=True, null=True)),
                ('day4', models.IntegerField(blank=True, null=True)),
                ('day5', models.IntegerField(blank=True, null=True)),
                ('day6', models.IntegerField(blank=True, null=True)),
                ('day7', models.IntegerField(blank=True, null=True)),
                ('day8', models.IntegerField(blank=True, null=True)),
                ('day9', models.IntegerField(blank=True, null=True)),
                ('day10', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
