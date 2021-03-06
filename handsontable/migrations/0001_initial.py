# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-28 06:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, verbose_name='Product_Name')),
                ('purchase_date', models.DateTimeField(verbose_name='Date')),
                ('customer_name', models.CharField(max_length=255, verbose_name='Customer_Name')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_at', models.DateTimeField(verbose_name='UpdateAt')),
            ],
        ),
        migrations.AddField(
            model_name='detail',
            name='header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handsontable.Header'),
        ),
    ]
