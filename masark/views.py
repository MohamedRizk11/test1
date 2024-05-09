from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Station
from .serializer import YourModelSerializer

class YourModelAPIView(APIView):
    def get(self, request):
        queryset = Station.objects.all()
        serializer = YourModelSerializer(queryset, many=True)
        return Response(serializer.data)
