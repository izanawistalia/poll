# Generated by Django 3.0.8 on 2020-08-07 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0003_candidates_expert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialty',
            name='name',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='subject',
        ),
        migrations.DeleteModel(
            name='candidates',
        ),
        migrations.DeleteModel(
            name='expertise',
        ),
        migrations.DeleteModel(
            name='specialty',
        ),
    ]
