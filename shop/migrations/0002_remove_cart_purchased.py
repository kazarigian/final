# Generated by Django 4.1.3 on 2022-12-01 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='purchased',
        ),
    ]