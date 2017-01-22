# coding=utf-8
from django.core.management.base import BaseCommand
from django.core.files import File
from app.models import Brand, Bike
from django.contrib.auth.models import User
import random


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    brands = [{'name': 'Kona', 'logo': 'app/static/images/kona_logo.jpg'},
              {'name': 'Scott', 'logo': 'app/static/images/scott_logo.jpg'}]
    brandsModel = []

    def _create_brands(self):
        for brandInfo in self.brands:
            brand = Brand()
            brand.name = brandInfo['name']
            logo = File(open(brandInfo['logo'], 'rb'))
            brand.image.save(logo.name, logo)
            brand.save()

            self.brandsModel.append(brand)

    def _create_bikes(self):
        user = User.objects.get(pk=1)

        for i in range(1, 40):
            for brand in self.brandsModel:
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
                    open('app/static/images/' + brand.name.lower() + '_' + str(random.choice(range(1, 2))) + '.jpg',
                         'rb')))

                bike.save()

    def handle(self, *args, **options):
        try:
            print('Executing seeds')
            User.objects.create_superuser('demo', 'demo@demo.com', 'demo')
            self._create_brands()
            self._create_bikes()
            print('Seeds executed')
        except Exception:
            print('Seeds not executed because were already executed')
