from django.urls import path

from . import views

app_name = "chat"
urlpatterns = [
    path("", views.IndexViews.as_view()),
    path("test/", views.test_api),
    path("login/", views.login_view),
    path("logout/", views.logout_view),
    path("room/<int:room_id>/", views.RoomViews.as_view(), name="room"),
]