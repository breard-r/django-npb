from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='npb_index'),
]
