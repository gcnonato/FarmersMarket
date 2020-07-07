from django.contrib import admin

from trader.models import TraderInfo, MarketInfo

# Register your models here.

admin.site.register(TraderInfo)
admin.site.register(MarketInfo)
