from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"), 
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events/', views.all_events, name="list-events"),
    path('add_eventlocation/', views.add_eventlocation, name='add-eventlocation'),
    path('list_eventlocations/', views.list_eventlocations, name='list-eventlocations'),
    path('show_location/<location_id>/', views.show_location, name='show-location'),
    path('update_location/<location_id>/', views.update_location, name='update-location'),
    path('add_event/', views.add_event, name='add-event'),
    path('update_event/<event_id>/', views.update_event, name='update-event'),
    path('delete_event/<event_id>/', views.delete_event, name='delete-event'),
    path('delete_location/<location_id>/', views.delete_location, name='delete-location')
]