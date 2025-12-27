from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from django.db import transaction
from ..models import Ticket
from django.shortcuts import get_object_or_404
from users.permissions import IsStaff


class ScanTicketView(APIView):
     permission_classes = [IsStaff]

     def post(self, request, qr_code, *args, **kwargs):
          with transaction.atomic():
              ticket = Ticket.objects.select_for_update().get(qr_code=qr_code)
              if ticket.is_used:
               raise ValidationError("This ticket has already been used")
              ticket.is_used = True
              ticket.save()          
          return Response(
               {
                    'message':'the ticket has been scanned successfully'
               },
               status=status.HTTP_200_OK
          )