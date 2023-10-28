from django.urls import path

from . import views

app_name = "chat"
urlpatterns = [
    path("", views.IndexViews.as_view(), name="index"),
    path("test/", views.test_api, name="test"),
]