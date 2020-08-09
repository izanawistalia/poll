# Generated by Django 3.0.8 on 2020-08-07 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidate', '0004_auto_20200807_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='candidates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('challenges_solved', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='expertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=5, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.candidates')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.expertise')),
            ],
        ),
        migrations.AddField(
            model_name='candidates',
            name='expert',
            field=models.ManyToManyField(through='candidate.specialty', to='candidate.expertise'),
        ),
    ]
