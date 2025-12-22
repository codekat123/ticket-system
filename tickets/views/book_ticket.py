from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Ticket
from ..serializers import TicketSerializer
from events.models import Event
from ..services import create_ticket_and_send_it


class TicketAPIView(APIView):

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)

        serializer = TicketSerializer(data=request.data,context={"event": event})
        serializer.is_valid(raise_exception=True)

        ticket = create_ticket_and_send_it(serializer,event)

        return Response(
            TicketSerializer(ticket).data,
            status=status.HTTP_201_CREATED
        )
