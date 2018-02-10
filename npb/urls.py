from django.urls import path
from . import views


app_name = 'npb'

urlpatterns = [
    path('', views.CreatePasteView.as_view(), name='index'),
    path('show/<uuid:pk>/', views.ShowPasteView.as_view(), name='show_paste'),
]
