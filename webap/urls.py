from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

app_name = "webap"

urlpatterns = [
    path("", WebAppIndex.as_view(), name="index"),
    path("event", csrf_exempt(WebAppIndex.as_view()), name="index/event"),
]