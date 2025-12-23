from rest_framework.views import APIView
from rest_framework.response import Response
from users.permissions import IsAdmin
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q
from ..models import Event
from tickets.models import Ticket


class AdminEventDetailView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)

        ticket_stats = Ticket.objects.filter(
            event=event
        ).aggregate(
            total=Count("id"),
            used=Count("id", filter=Q(is_used=True)),
            unused=Count("id", filter=Q(is_used=False)),
        )

        response_data = {
            "event": {
                "id": event.id,
                "title": event.title,
                "location": event.location,
                "start_date": event.start_date,
                "end_date": event.end_date,
                "capacity": event.capacity,
                "is_active": event.is_active,
            },
            "tickets": {
                "total": ticket_stats["total"],
                "used": ticket_stats["used"],
                "unused": ticket_stats["unused"],
                "remaining_capacity": max(
                    event.capacity - ticket_stats["total"],0
                ),
                "check_in_rate": (
                    ticket_stats["used"] / ticket_stats["total"] * 100
                    if ticket_stats["total"] > 0 else 0
                ),
            }
        }

        return Response(response_data)
