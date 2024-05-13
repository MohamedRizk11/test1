from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Station,Road,Ticket,Users,FamousPlace
from .serializer import StationSerializer,RoadSerializer,TicketSerializer,UsersSerializer,FamousPlaceSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# في views.py
import json
from django.http import JsonResponse
from django.views import View
from .utils import voice_search_database
class VoiceSearchAPI(View):
    def get(self, request, *args, **kwargs):
        # تنفيذ البحث الصوتي عند استلام طلب GET
        results = voice_search_database()
        
        if results:
            result = results[0][0]  # استخدام النتيجة الأولى
        else:
            result = "لا توجد نتائج."
        
        # إعداد البيانات التي ستُرجع كاستجابة للطلب
        data = {
            'status': 'success',
            'result': result  # إضافة النتائج
        }
        return JsonResponse(data, charset='utf-8')

    def post(self, request, *args, **kwargs):
        # تنفيذ البحث الصوتي عند استلام طلب POST
        results = voice_search_database()
        
        if results:
            result = results[0][0]  # استخدام النتيجة الأولى
        else:
            result = "لا توجد نتائج."
        
        # إعداد البيانات التي ستُرجع كاستجابة للطلب
        data = {
            'status': 'success',
            'result': result  # إضافة النتائج
        }
        return JsonResponse(data, charset='utf-8')








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
 