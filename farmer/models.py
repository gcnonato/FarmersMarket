from django.db import models
from django.conf import settings
from django.urls import reverse_lazy

# Create your models here.

class ProductInfo(models.Model):
    product_name = models.CharField(max_length=255, blank=False)
    unit_of_measure = models.CharField(max_length=50)
    brief_description = models.TextField(blank=True, default='')
    minimum_price = models.IntegerField(blank=False, default='0')
    quantity_available = models.IntegerField(blank=False, default="0")
    negotiable = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.product_name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse_lazy("groups:single", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["product_name"]



class FarmerInfo(models.Model):
    full_names = models.CharField(max_length=255)
    telephone_number = models.IntegerField(blank=False, unique=True, default='0775058319')
    farm_product = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pics/farmer_pics', blank=True)

    def __str__(self):
        return self.full_names

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('trader:all_traders')
