# Generated by Django 3.0.8 on 2020-08-08 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0006_auto_20200807_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidates',
            name='votes',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
