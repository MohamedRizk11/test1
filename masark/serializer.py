from rest_framework import serializers
from .models import Station , Road ,Ticket,Users,FamousPlace

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'



class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = '__all__'        


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'  


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'  


class FamousPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamousPlace
        fields = '__all__'  