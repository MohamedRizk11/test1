from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Station,Road,Ticket,Users,FamousPlace
from .serializer import StationSerializer,RoadSerializer,TicketSerializer,UsersSerializer,FamousPlaceSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class StationAPIView(APIView):
    def get(self, request):
        queryset = Station.objects.all()
        serializer = StationSerializer(queryset, many=True)
        return Response(serializer.data)
    search_fields = ['id', 'email']
    
class RoadAPIView(APIView):
    def get(self, request):
        queryset = Road.objects.all()
        serializer = RoadSerializer(queryset, many=True)
        return Response(serializer.data)   


class TicketAPIView(APIView):
    def get(self, request):
        queryset = Ticket.objects.all()
        serializer = TicketSerializer(queryset, many=True)
        return Response(serializer.data)      


class UsersAPIView(APIView):
    def get(self, request):
        queryset = Users.objects.all()
        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)  
    

class FamousPlaceAPIView(APIView):
    def get(self, request):
        queryset = FamousPlace.objects.all()
        serializer =FamousPlaceSerializer(queryset, many=True)
        return Response(serializer.data)      