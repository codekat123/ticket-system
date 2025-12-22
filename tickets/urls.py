from django.urls import path
from .views import (
     TicketAPIView,
     ScanTicketView,
)


app_name='tickets'

urlpatterns = [
     path('book/<int:event_id>/',TicketAPIView.as_view(),name='book'),
     path('scan/<qr_code>/',ScanTicketView.as_view(),name='scan'),
]