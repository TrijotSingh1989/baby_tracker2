from django.urls import path
from . import views

urlpatterns = [
    path('add/<str:event_type>/', views.add_event, name='add_event'),
    path('events/', views.event_list, name='event_list'),
]
