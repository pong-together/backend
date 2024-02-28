# Generated by Django 5.0.1 on 2024-02-28 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1_name', models.CharField(max_length=10)),
                ('player2_name', models.CharField(max_length=10)),
                ('game_mode', models.CharField(choices=[('default', 'Default'), ('extreme', 'Extreme')], max_length=7)),
            ],
        ),
    ]