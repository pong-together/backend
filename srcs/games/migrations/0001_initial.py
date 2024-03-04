# Generated by Django 5.0.1 on 2024-03-04 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1_name', models.CharField()),
                ('player2_name', models.CharField()),
                ('player1_score', models.IntegerField(default=0)),
                ('player2_score', models.IntegerField(default=0)),
                ('player1_y', models.IntegerField()),
                ('player2_y', models.IntegerField()),
                ('ball_x', models.IntegerField()),
                ('ball_y', models.IntegerField()),
            ],
        ),
    ]