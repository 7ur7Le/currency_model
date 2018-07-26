from django.urls import path

from . import views

urlpatterns = [
    path('pair_detail/', views.pair_detail, name='pair_detail'),
]