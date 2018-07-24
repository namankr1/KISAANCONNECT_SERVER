# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorization', '0001_initial'),
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=70)),
                ('quantity', models.FloatField()),
                ('price', models.FloatField()),
                ('description', models.TextField(default=None, null=True)),
                ('bidvalue', models.FloatField(default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.Profile')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorization.Subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.Profile')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorization.Subcategory')),
            ],
        ),
    ]
