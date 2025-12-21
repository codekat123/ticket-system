from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls',namespace='users')),
    path('events/',include('events.urls',namespace='events')),
    path('tickets/',include('tickets.urls',namespace='tickets')),
]
