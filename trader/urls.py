from django.conf.urls import url
from . import views

app_name='trader'

urlpatterns = [
    url(r"^$", views.TraderList.as_view(), name="all_traders"),
    url(r"new/$", views.RegisterTrader.as_view(), name="trader_registration"),
    url(r'^(?P<pk>\d+)/$', views.TraderDetails.as_view(), name='trader_detail'),
    # url(r"details",views.FarmerDetail.as_view(),name="farmer"),
]
