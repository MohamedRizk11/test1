from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Station,Road
from .serializer import StationSerializer,RoadSerializer

class StationAPIView(APIView):
    def get(self, request):
        queryset = Station.objects.all()
        serializer = StationSerializer(queryset, many=True)
        return Response(serializer.data)
    
class RoadAPIView(APIView):
    def get(self, request):
        queryset = Road.objects.all()
        serializer = RoadSerializer(queryset, many=True)
        return Response(serializer.data)    
