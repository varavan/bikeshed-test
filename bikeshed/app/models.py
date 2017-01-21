from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(default="", upload_to='brand_logo')
    image_thumbnail = ResizedImageField(size=[150, 150], upload_to='brand_logo_thumbnail', default="")
    image_small = ResizedImageField(size=[262, 190], upload_to='brand_logo_small', default="")
    image_big = ResizedImageField(size=[570, 400], upload_to='brand_logo_big', default="")
    def __str__(self):
        return self.name

class Bike(models.Model):
    brand = models.ForeignKey(Brand)
    type = models.CharField(max_length=10, choices=(("mountain", "Mountain"), ('road', 'Road'), ('hybrid', 'Hybrid')))
    #created_by = models.CharField() by (FK to User)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    model = models.CharField(max_length=255)
    headline = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(default="", upload_to='bike')
    image_thumbnail = ResizedImageField(size=[150,150], upload_to='bike_thumbnail', default="")
    image_small = ResizedImageField(size=[262, 190], upload_to='bike_small', default="")
    image_big = ResizedImageField(size=[570, 400], upload_to='bike_big', default="")
    size = models.IntegerField() # (int, max 30, min 12)
    price = models.DecimalField(decimal_places=2, max_digits=15)

    def __str__(self):
        return self.model