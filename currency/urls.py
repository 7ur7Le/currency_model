try:
    from django.urls import include, path
except ImportError:
    from django.conf.urls import include
    from django.conf.urls import url as path
from . import views


urlpatterns = [
    path('pair_detail/', views.pair_detail, name='pair_detail'),
]