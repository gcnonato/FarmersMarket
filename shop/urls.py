from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'shop'

urlpatterns = [
    url(r'^products/$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

    url(r"login/$", views.LoginUserView.as_view(),name='shop_login'),
    url(r"logout/$", auth_views.LogoutView.as_view(), name="shop_logout"),
    url(r"signup/$", views.signup, name="shop_signup"),
]