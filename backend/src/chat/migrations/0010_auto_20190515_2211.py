# Generated by Django 2.1.7 on 2019-05-15 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_auto_20190515_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mood',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
