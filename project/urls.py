"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from masark.views import StationAPIView,RoadAPIView,TicketAPIView,UsersAPIView,FamousPlaceAPIView,VoiceSearchAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Stationapi/', StationAPIView.as_view()),
    path('Roadapi/', RoadAPIView.as_view()),
    path('ticketapi/', TicketAPIView.as_view()),
    path('usersapi/', UsersAPIView.as_view()),
    path('famousplacesapi/', FamousPlaceAPIView.as_view()),

    path('voice_search/', VoiceSearchAPI.as_view(), name='voice_search'),
]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





