"""FarmersMarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.conf import settings

# To use the built in user authentication module.
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView, LoginView
from django.conf.urls.static import static

urlpatterns = [
    url(r"^$", views.HomePage.as_view(), name="home"),
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r"^thanks/$", views.ThanksPage.as_view(), name="shop_thanks"),
    path('admin/', admin.site.urls),
    url(r"^farmer/", include("farmer.urls", namespace="farmer")),
    url(r"^trader/", include("trader.urls", namespace="trader")),
    url(r"^blog/", include("blog.urls", namespace="blog")),

    url(r'^login/$', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    url(r"^blog/", include("django.contrib.auth.urls")),

    url('cart', include('cart.urls')),
    url('orders/', include('orders.urls')),
    url('shop/', include('shop.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
