# Generated by Django 5.0 on 2024-09-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0002_alter_gorod_options_alter_status_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cars",
            name="god_vypuska",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
