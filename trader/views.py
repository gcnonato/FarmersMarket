from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView
from trader import models

# Create your views here.


class TraderList(ListView):
    """docstring for Trader."""

    context_object_name = 'traders'
    model = models.TraderInfo
    template_name = 'trader/traders_list.html'

class RegisterTrader(CreateView):
    """docstring for RegisterTrader."""

    model = models.TraderInfo
    fields = ('full_names', 'telephone_number', 'vending_product', 'market_location', 'profile_pic')
    template_name = 'trader/trader_form.html'

class TraderDetails(DetailView):
    """docstring for TraderDetailsView."""

    # By default, a detail view returns a lower case version of the model. Eg, in this case,
    # the default view returned will be named as school.

    context_object_name = 'trader_details'
    model = models.TraderInfo
    template_name = 'trader/trader_details.html'
