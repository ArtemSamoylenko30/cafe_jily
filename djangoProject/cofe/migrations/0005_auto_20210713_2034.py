# Generated by Django 3.2.4 on 2021-07-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cofe', '0004_res'),
    ]

    operations = [
        migrations.AlterField(
            model_name='res',
            name='date_reg',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='res',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]