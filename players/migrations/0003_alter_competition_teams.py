# Generated by Django 4.1.2 on 2023-02-28 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0002_competition"),
    ]

    operations = [
        migrations.AlterField(
            model_name="competition",
            name="teams",
            field=models.ManyToManyField(blank=True, to="players.team"),
        ),
    ]
