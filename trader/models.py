from django.db import models
from django.conf import settings
from django.urls import reverse_lazy

from farmer.models import ProductInfo

# Create your models here.


class MarketInfo(models.Model):
    market_name = models.CharField(max_length=255)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.market_name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)


class TraderInfo(models.Model):
    full_names = models.CharField(max_length=255)
    telephone_number = models.IntegerField(blank=False, unique=True, default='0756479646')
    vending_product = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    market_location = models.ForeignKey(MarketInfo, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/trader_pics', blank=True)

    def __str__(self):
        return self.full_names

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy("farmer:all")
