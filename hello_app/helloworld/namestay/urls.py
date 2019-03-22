
from django.urls import path

from . import views
urlpatterns = [
    path('',views.namestay_homePage, name='home'),
]
