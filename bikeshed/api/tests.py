# coding=utf-8
from django.test import TestCase
from app.builders import build_random_bike_with_random_user
from .factories import bike_view_factory


class FactoryTestCase(TestCase):
    def test_bike_view_factory(self):
        bike = build_random_bike_with_random_user()

        bikeBuild = bike_view_factory(bike)

        self.assertEqual(bike.model, bikeBuild['model'])
        self.assertEqual(bike.price, bikeBuild['price'])
        self.assertEqual(bike.brand.name, bikeBuild['brand'])
        self.assertEqual(bike.headline, bikeBuild['headline'])
        self.assertEqual(bike.description, bikeBuild['description'])
        self.assertEqual(bike.created_by.email, bikeBuild['created_by'])
        self.assertEqual(bike.id, bikeBuild['id'])
