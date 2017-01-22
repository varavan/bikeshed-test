# coding=utf-8
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from django.core.files import File
from app.models import Brand
from django.contrib.auth.models import User
from app.builders import build_random_bike_with_user_and_brand, build_superuser


class Command(BaseCommand):
    help = 'Populates database with demo data'

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
                build_random_bike_with_user_and_brand(user, brand)

    def handle(self, *args, **options):
        try:
            print('Executing seeds')
            build_superuser('demo', 'demo', 'demo@demo.com')
            self._create_brands()
            self._create_bikes()
            print('Seeds executed')
        except IntegrityError:
            print('Seeds not executed because were already executed')
