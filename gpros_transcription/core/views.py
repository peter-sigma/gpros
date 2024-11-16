from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'core/index.html'  # Specify the template to load
