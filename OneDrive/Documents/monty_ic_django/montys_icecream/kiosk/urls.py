from django.urls import path
from . import views

urlpatterns = [
   path('', views.menu, name='menu'),
    # other app-specific URLs
]
