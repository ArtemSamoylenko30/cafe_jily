from django.db import models
from uuid import uuid4
from os import path
from django.core.validators import RegexValidator
import datetime
# Create your models here.

class Category(models.Model):
    title = models.CharField(unique=True, max_length=50)
    is_visible = models.BooleanField(default=True)
    cat_order = models.PositiveIntegerField(unique=True)

    def __str__(self):

        return f'{self.title} - {self.cat_order}'

class Dish(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/dishes', filename)

    title = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    dish_order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.CharField(max_length=100)
    desc = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}: {self.price}'


class About(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/about', filename)

    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    media_url = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.title}'

class Res(models.Model):
    mobile_regex = RegexValidator(regex=r'^(\d{3}[- .]?{2}\d{4}$)', message=' Phone in format xxx xxx xxxx ')
    time_visit = models.DateTimeField(auto_now=True)
    timi_proc = models.BooleanField(default=False)
    your_name = models.CharField(max_length=100)
    your_email = models.EmailField()
    date_reg = models.DateField()
    date_time = models.DateTimeField()
    number_tel = models.CharField(max_length=12, unique=True)
    of_people = models.PositiveIntegerField()
    message = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.your_name} : {self.your_email} : {self.message[:20]}'

class Res_1(models.Model):
    your_name = models.CharField(max_length=100)
    your_email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=400)

    time_visit = models.DateTimeField(auto_now=True)
    is_proc = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.your_name} : {self.your_email} : {self.message[:20]}'