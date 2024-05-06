from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models


Status_type=(
    ("Normal","Normal"),
    ("Disabled","Disabled"),

)

class Users(models.Model):
    user_id=models.IntegerField(_("User_ID"),primary_key=True)
    status=models.CharField(_("Status"),max_length=10,choices=Status_type)

    def __str__(self):
        return str(self.user_id)
class Station(models.Model):
    id=models.IntegerField(_("Id"),unique=True,primary_key=True)
    geom = models.PointField(srid=4326) 
    fid=models.IntegerField(_("Fid"))
    station_id=models.IntegerField(_("Station_id"))
    name=models.CharField(_("Name"),max_length=40)
    def __str__(self):
        return self.name
class FamousPlace(models.Model):
    station = models.ForeignKey("Station", related_name='station_place', on_delete=models.SET_NULL,null=True)
    name = models.CharField(_("Name"),max_length=100)

    def __str__(self):
        return self.name
    

class Road(models.Model):
    id=models.IntegerField(_("Id"),unique=True,primary_key=True) 
    geom = models.PointField(srid=4326)
    fid=models.IntegerField(_("Fid"))
    road_id=models.IntegerField(_("road_id"))
    name=models.CharField(_("Name"),max_length=40)  
    time=models.IntegerField()
    distance=models.FloatField() 

class Ticket(models.Model):
    from_station = models.ForeignKey(Station, related_name='from_station', on_delete=models.SET_NULL,null=True)
    to_station = models.ForeignKey(Station, related_name='to_station', on_delete=models.SET_NULL,null=True)
    cost = models.IntegerField(_("Cost"))
    time = models.FloatField(_("Time"))


    

    
        
