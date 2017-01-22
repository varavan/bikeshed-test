# coding=utf-8
from django.core.files import File
from django.contrib.auth.models import User
import random

from app.models import Bike, Brand


def build_superuser(user, password, email):
    return User.objects.create_superuser(user, email, password)


def build_random_brand():
    brand = Brand()
    brand.name = 'Scott'

    brand.save()
    return brand


def build_random_bike_with_random_user():
    bike = build_random_bike_with_user_and_brand(
        build_superuser('root', 'root', 'root@test.com'),
        build_random_brand())
    bike.save()

    return bike


def build_random_bike_with_user_and_brand(user, brand):
    bike = Bike()

    bike.brand = brand
    bike.created_by = user
    bike.type = random.choice(['mountain', 'road', 'hybrid'])
    bike.size = random.choice(range(12, 30))
    bike.model = random.choice(['Scott Adict', 'Scott Voltage', 'Kona Stinky', 'Kona Stuff'])
    bike.headline = "Awesome Bike"
    bike.description = "Awesome test bike"
    bike.price = (random.choice(range(100, 999999))) / 100
    bike.setImage(File(
        open(
            'app/static/images/%s_%s.jpg' % (
                brand.name.lower(),
                str(random.choice(range(1, 2)))
            ),
            'rb')))

    bike.save()

    return bike
