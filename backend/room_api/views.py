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
            return JsonResponse("Room Added Successfully", safe = False)
        return JsonResponse("Attempt to add Room failed", safe = False)
    elif request.method == "PUT":
        room_data = JSONParser().parse(request)
        room = Room_Features.objects.get(room_id=room_data['room_id'])
        room_serializer = RoomSerializer(room, data=room_data)
        if room_serializer.is_valid():
            room_serializer.save()
            return JsonResponse("Room Updated Success", safe = False)
        return JsonResponse("Room Update Failed")
    elif request.method == 'DELETE':
        if not id:
            return JsonResponse("Please Provide a valid ID", safe = False)
        room = Room_Features.objects.get(room_id = id)
        room.delete()
        return JsonResponse("Room Deleted Success", safe = False)

# API methods for Reservation table 
@csrf_exempt
def ReservationAPI(request, id=0):
    if request.method == 'GET':
        reservation = Reservations.objects.all()
        reservation_serializer = ReservationSerializer(reservation, many = True)
        return JsonResponse(reservation_serializer.data, safe = False)
    elif request.method == 'POST':
        reservation_data = JSONParser().parse(request)
        reservation_serializer = ReservationSerializer(data = reservation_data)
        if reservation_serializer.is_valid():
            reservation_serializer.save()
            return JsonResponse("Reservation Added Successfully", safe = False)
        return JsonResponse("Attempt to add Reservation failed", safe = False)
    elif request.method == "PUT":
        reservation_data = JSONParser().parse(request)
        reservation = Reservations.objects.get(res_id=reservation_data['res_id'])
        reservation_serializer = ReservationSerializer(reservation, data=reservation_data)
        if reservation_serializer.is_valid():
            reservation_serializer.save()
            return JsonResponse("Reservation Updated Success", safe = False)
        return JsonResponse("Reservation Update Failed")
    elif request.method == 'DELETE':
        if not id:
            return JsonResponse("Please Provide a valid ID", safe = False)
        reservation = Reservations.objects.get(res_id = id)
        reservation.delete()
        return JsonResponse("Reservation Deleted Success", safe = False)



