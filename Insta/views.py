from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class Helloworld(TemplateView):
    template_name = 'test.html'