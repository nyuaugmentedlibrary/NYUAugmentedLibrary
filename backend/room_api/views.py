# API methods
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from room_api.models import Room_Features, Reservations
from room_api.serializers import RoomSerializer, ReservationSerializer

# API methods for Room_features table 
@csrf_exempt
def RoomAPI(request, id=0):
    if request.method == 'GET':
        room = Room_Features.objects.all()
        room_serializer = RoomSerializer(room, many = True)
        return JsonResponse(room_serializer.data, safe = False)
    elif request.method == 'POST':
        room_data = JSONParser().parse(request)
        room_serializer = RoomSerializer(data = room_data)
        if room_serializer.is_valid():
            room_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Attempt to add failed", safe = False)
    elif request.method == "PUT":
        room_data = JSONParser().parse(request)
        room = Room_Features.objects.get(room_id=room_data['room_id'])
        room_serializer = room_serializer(room, data=room_data)
        if room_serializer.is_valid():
            room_serializer.save()
            return JsonResponse("Update Success", safe = False)
        return JsonResponse("Update Failed")
    elif request.method == 'DELETE':
        room == Room_Features.objects.get(room_id = id)
        room.delete()
        return JsonResponse("Delete Success", safe = False)



