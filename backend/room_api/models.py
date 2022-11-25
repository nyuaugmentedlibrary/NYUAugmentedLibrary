from django.db import models

# Create your models here.
class Room_Features(models.Model):
    room_id = models.AutoField(primary_key=True)
    monitor = models.BooleanField()

class Reservations(models.Model):
    room_id = models.ForeignKey(Room_Features, on_delete=models.CASCADE)
    res_id = models.AutoField(primary_key=True)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()

    
