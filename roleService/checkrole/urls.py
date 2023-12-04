from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('getRole/', csrf_exempt(views.getRole), name='getRole'),
]