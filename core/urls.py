from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('checkout', checkout, name='checkout'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
]
