# Generated by Django 3.0.8 on 2020-08-07 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0005_auto_20200807_1547'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='specialty',
            unique_together={('name', 'subject')},
        ),
    ]
