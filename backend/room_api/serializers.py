# Help to convert model instances into native python types
# Which can then be rendered into json
from rest_framework import serializers
from room_api.models import Room_Features, Reservations

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room_Features
        fields = ('room_id', 'monitor')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = ('room_id', 'res_id', 'start_date_time', 'end_date_time')