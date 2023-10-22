from django.test import TestCase
from .models import *
from django.contrib.auth import get_user, get_user_model
import datetime

User = get_user_model()
# Create your tests here.

class ModelTest(TestCase):
    def register_UserRoomChat(self):
        user = User(username="ioio", email="ioio@gmail.com", password="ioio432")
        room = Room(user=user, roomname="01")
        userchat = UserChat(room=room, content="hello", datetime=datetime.datetime.now())
        aichat = AIChat(room=room, content="こんにちは", datetime=datetime.datetime.now())