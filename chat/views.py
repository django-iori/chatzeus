from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.
class IndexViews(generic.TemplateView):
    template_name = "chat/index.html"