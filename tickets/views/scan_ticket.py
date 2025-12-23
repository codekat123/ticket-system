from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Ticket
from django.shortcuts import get_object_or_404


class ScanTicketView(APIView):

     def post(self,qr_code):
          ticket = get_object_or_404(Ticket,qr_code=qr_code)
          ticket.is_used = True
          ticket.save()          
          return Response(
               {
                    'message':'the ticket has been scanned successfully'
               },
               status=status.HTTP_200_OK
          )