from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
import time

# Create your views here.
class IndexViews(generic.TemplateView):
    template_name = "chat/index.html"

@api_view(['GET', 'POST'])
def test_api(request):
    if request.method == 'POST':
        print(request.data)
        time.sleep(1)
        dt = datetime.datetime.now()
        return Response(data={
            "message": "こんにちは", 
            "datetime": str(dt.hour) + ":" + str(dt.minute),
        })
    return Response(data={"message": "Hello, world!"})
