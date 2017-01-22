# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.core.validators import MaxValueValidator, MinValueValidator
import app.helpers


class Brand(models.Model):
    name = models.CharField(max_length=255)

    image = ResizedImageField(
        size=[150, 150],
        upload_to=app.helpers.sanitaze_image_upload_path,
        default=""
    )

    def __str__(self):
        return self.name


class Bike(models.Model):
    brand = models.ForeignKey(Brand)

    type = models.CharField(
        max_length=10,
        choices=(("mountain", "Mountain"), ('road', 'Road'), ('hybrid', 'Hybrid')))

    created_by = models.ForeignKey(User)

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False
    )

    model = models.CharField(
        max_length=255,
        blank=False
    )

    headline = models.CharField(
        max_length=100,
        blank=False
    )

    description = models.TextField(
        max_length=500,
        blank=False
    )

    image_thumbnail = ResizedImageField(
        size=[262, 190],
        upload_to=app.helpers.sanitaze_image_upload_path,
        default=""
    )

    image = ResizedImageField(
        size=[570, 400],
        upload_to=app.helpers.sanitaze_image_upload_path,
        blank=False
    )

    size = models.IntegerField(
        validators=[MaxValueValidator(30), MinValueValidator(12)],
        blank=False
    )

    price = models.DecimalField(
        decimal_places=2,
        max_digits=15
    )

    def setImage(self, image):
        self.image_thumbnail = image
        self.image = image

    def __str__(self):
        return self.model
