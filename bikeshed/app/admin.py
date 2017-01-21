from django.contrib import admin
from django import forms
from app.models import Brand

# Register your models here.

class BrandForm(forms.ModelForm):

    class Meta:
        fields = ['name', 'image']
        model = Brand

class BrandAdmin(admin.ModelAdmin):
    form = BrandForm

admin.site.register(Brand, BrandAdmin)