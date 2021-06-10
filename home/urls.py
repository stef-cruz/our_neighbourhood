from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('faq/',
         TemplateView.as_view(template_name='home/faq.html'),
         name='faq'),
]
