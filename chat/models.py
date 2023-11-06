from django.db import models
from django.contrib.auth import get_user, get_user_model

User = get_user_model()

# Create your models here.
class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roomname = models.CharField(max_length=30)

class Chat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    datetime = models.DateTimeField()
    is_AI = models.BooleanField(default=False, help_text='AIの回答ならTrue')