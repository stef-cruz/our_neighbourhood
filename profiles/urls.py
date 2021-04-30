from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('delete_profile/<str:user>',
         views.delete_profile, name='delete_profile'),
]
