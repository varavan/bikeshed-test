# coding=utf-8
from django.test import TestCase
from django.core.files import File

from .models import Bike
from .forms import BikeForm
from .helpers import sanitaze_image_upload_path

def anyFile():
    return File(open('app/static/images/kona_logo.jpg','rb'))

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
        path = sanitaze_image_upload_path('', 'test.jpeg')

        self.assertIsNotNone(path)