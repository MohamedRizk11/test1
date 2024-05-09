from django.contrib import admin
from .models import Ticket,Road,Station,FamousPlace,Users

# Register your models here.

admin.site.register(Station)
admin.site.register(Road)
admin.site.register(Ticket)
admin.site.register(FamousPlace)
admin.site.register(Users)