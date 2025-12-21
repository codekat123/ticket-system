from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Ticket
from .serializers import TicketSerializer
from events.models import Event


class TicketAPIView(APIView):

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)

        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ticket = serializer.save(event=event)

        return Response(
            TicketSerializer(ticket).data,
            status=status.HTTP_201_CREATED
        )
