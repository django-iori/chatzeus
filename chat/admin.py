from django.contrib import admin
from .models import *
from django.contrib.sessions.models import Session

# Register your models here.
admin.site.register(Room)
admin.site.register(Chat)
admin.site.register(Session)