# Generated by Django 5.1.4 on 2025-01-14 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('sleep', 'Sleep'), ('feed', 'Feed'), ('poop', 'Poop'), ('diaper_change', 'Diaper Change')], max_length=50)),
                ('event_time', models.DateTimeField(auto_now_add=True)),
                ('duration', models.DurationField(blank=True, null=True)),
            ],
        ),
    ]
