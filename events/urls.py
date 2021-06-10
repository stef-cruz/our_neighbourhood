from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('add_event', views.add_event, name='add_event'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('edit_event/<int:event_id>', views.edit_event, name='edit_event'),
    path('delete_event/<int:event_id>',
         views.delete_event, name='delete_event'),
    path('preview_event/<int:event_id>',
         views.preview_event, name='preview_event'),
]
