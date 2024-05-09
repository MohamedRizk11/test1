from rest_framework import serializers
from .models import Station , Road

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'



class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = '__all__'        
