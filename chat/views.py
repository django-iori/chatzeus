from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
import time
from .models import *
# Create your views here.
class IndexViews(LoginRequiredMixin, generic.ListView):
    login_url = "/login/"
    model = Room
    context_object_name = 'rooms'
    template_name = "chat/index.html"

    def get_queryset(self):
        return Room.objects.filter(user=self.request.user)


class RoomViews(LoginRequiredMixin, generic.ListView):
    login_url = "/login/"
    model = Room
    context_object_name = 'rooms'
    template_name = "chat/room.html"

    def get_context_data(self, *args, **kwargs):
        room_id = self.kwargs['room_id']
        context = super().get_context_data(*args, **kwargs)
        context['chats'] = Chat.objects.filter(room=room_id)
        context['room'] = Room.objects.get(pk=room_id)
        return context


def test_api(request):
    if request.method == 'POST':
        print("request: ", request.POST['content'])
        time.sleep(1)
        dt = datetime.datetime.now()
        return JsonResponse({
            "message": "こんにちは", 
            "datetime": str(dt.hour) + ":" + str(dt.minute),
        })
    return JsonResponse({"message": "Hello, world!"})

def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user.username)
            return redirect('/')
        else:
            return redirect('/login')
        
    return render(request, 'chat/login.html')

def logout_view(request):
    logout(request)
    return redirect('/login')