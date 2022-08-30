# Generated by Django 4.0.6 on 2022-08-30 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToMeet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persone', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('date_of_meeting', models.DateTimeField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
