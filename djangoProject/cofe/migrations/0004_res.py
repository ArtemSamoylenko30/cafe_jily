# Generated by Django 3.2.4 on 2021-07-13 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cofe', '0003_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Res',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_visit', models.DateTimeField(auto_now=True)),
                ('timi_proc', models.BooleanField(default=False)),
                ('your_name', models.CharField(max_length=100)),
                ('your_email', models.EmailField(max_length=254)),
                ('date_reg', models.DateField(auto_now=True)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('number_tel', models.CharField(max_length=12, unique=True)),
                ('of_people', models.PositiveIntegerField()),
                ('message', models.CharField(max_length=400)),
            ],
        ),
    ]
