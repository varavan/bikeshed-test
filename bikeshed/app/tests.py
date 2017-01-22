# coding=utf-8
from django.test import TestCase
from django.core.files import File

from app.models import Bike
from app.forms import BikeForm
from app.helpers import sanitaze_image_upload_path
from app.builders import build_superuser, build_random_brand, build_random_bike_with_random_user, \
    build_random_bike_with_user_and_brand


def anyFile():
    return File(open('app/static/images/kona_logo.jpg', 'rb'))


class BikeTestCase(TestCase):
    def test_image_and_thumbnail_are_set(self):
        object = Bike()
        object.setImage(anyFile())
        self.assertIsNotNone(object.image.url)
        self.assertIsNotNone(object.image_thumbnail.url)


class BikeFormTestCase(TestCase):
    def test_on_pass_image_set_image_method_is_call(self):
        form = BikeForm({}, {'image': anyFile()})
        self.assertIsNotNone(form.instance.image.url)
        self.assertIsNotNone(form.instance.image_thumbnail.url)


class HelpersTestCase(TestCase):
    def test_sanitaze_image_upload_path(self):
        path = sanitaze_image_upload_path('', 'test.tricky.name.jpeg')

        self.assertIsNotNone(path)
        self.assertEqual(path.count('image-upload'), 1)
        self.assertEqual(path.count('.jpeg'), 1)


class BuildersTestCase(TestCase):
    def test_build_superuser(self):
        username = 'username'
        password = 'password'
        email = 'email'

        user = build_superuser(username, password, email)

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertGreater(user.id, 0)

    def test_build_random_brand(self):
        brand = build_random_brand()

        self.assertIsNotNone(brand.name)
        self.assertGreater(brand.id, 0)

    def test_build_random_bike(self):
        bike = build_random_bike_with_random_user()

        self.assertIsNotNone(bike.headline)
        self.assertIsNotNone(bike.price)
        self.assertIsNotNone(bike.model)
        self.assertIsNotNone(bike.created_by)
        self.assertIsNotNone(bike.created_by.email)
        self.assertIsNotNone(bike.brand.name)

    def test_build_bike_with_brand_and_user(self):
        brand = build_random_brand()
        user = build_superuser('random_bike_and_user', 'random', 'random_bike_and_user@fake.com')

        bike = build_random_bike_with_user_and_brand(user, brand)

        self.assertIsNotNone(bike.headline)
        self.assertIsNotNone(bike.price)
        self.assertIsNotNone(bike.model)
        self.assertIsNotNone(bike.created_by)
        self.assertEqual(bike.created_by, user)
        self.assertEqual(bike.brand, brand)
