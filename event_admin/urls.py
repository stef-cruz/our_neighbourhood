from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_admin, name='event_admin'),
    path('mark_as_resolved/<int:contact_id>/', views.mark_as_resolved, name='mark_as_resolved'),
    path('mark_as_paid/<int:event_id>/', views.mark_as_paid, name='mark_as_paid'),
]
