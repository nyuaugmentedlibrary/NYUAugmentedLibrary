# Here are the routes to specify the url for API method for room_api
from django.urls import re_path
from room_api import views

urlpatterns = [
    # declare url route to call Room_Feature table's API methods
    re_path(r'^room$', views.RoomAPI),
    re_path(r'^room/([0-9]+)$',views.RoomAPI)
    
]