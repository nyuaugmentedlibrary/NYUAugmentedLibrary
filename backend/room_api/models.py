from django.db import models

"""
This is where the model of the relational database defined
Models basically tells Postgresql how the data is going to be organized
"""

class Room_Features(models.Model):
    room_id = models.AutoField(primary_key=True)
    monitor = models.BooleanField()

class Reservations(models.Model):
    room_id = models.ForeignKey(Room_Features, on_delete=models.DO_NOTHING)
    res_id = models.AutoField(primary_key=True)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()


    

    
