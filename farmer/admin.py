from django.contrib import admin

from farmer import models

# Register your models here.

admin.site.register(models.FarmerInfo)
admin.site.register(models.ProductInfo)
