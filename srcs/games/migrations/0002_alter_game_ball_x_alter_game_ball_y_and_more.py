# Generated by Django 5.0.1 on 2024-03-05 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='ball_x',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='ball_y',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='player1_y',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='player2_y',
            field=models.IntegerField(null=True),
        ),
    ]