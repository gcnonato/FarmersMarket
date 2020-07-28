from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from farmer import models

# Create your views here.

class FarmerList(ListView):
    """docstring for Farme."""

    context_object_name = 'farmers'
    model = models.FarmerInfo
    template_name = 'farmer/farmers_list.html'

class RegisterFarmer(CreateView):
    """docstring for RegisterFarmer."""

    model = models.FarmerInfo
    fields = ('full_names', 'telephone_number', 'farm_product', 'location', 'profile_pic')
    template_name = 'farmer/farmer_form.html'

class FarmerDetails(DetailView):
    """docstring for FarmerDetailsView."""

    # By default, a detail view returns a lower case version of the model. Eg, in this case,
    # the default view returned will be named as farmerdetails.

    context_object_name = 'farmer_details'
    model = models.FarmerInfo
    template_name = 'farmer/farmers_details.html'
