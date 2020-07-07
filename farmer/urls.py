from django.conf.urls import url

from . import views

app_name='farmer'

urlpatterns = [
    url(r"^$", views.FarmerList.as_view(), name="all"),
    url(r"new/$", views.RegisterFarmer.as_view(), name="farmer_registration"),
    url(r'^(?P<pk>\d+)/$', views.FarmerDetails.as_view(), name='farmer_detail'),
    # url(r"details",views.FarmerDetail.as_view(),name="farmer"),
]
