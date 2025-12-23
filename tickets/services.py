from rest_framework.exceptions import ValidationError
from django.db import transaction
from .models import Ticket
from .tasks import send_ticket_email

@transaction.atomic
def create_ticket_and_send_it(serializer, event):
    tickets_count = Ticket.objects.filter(event=event).count()

    if tickets_count >= event.capacity:
        raise ValidationError("All tickets are already sold.")

    ticket = serializer.save(event=event)
    send_ticket_email(ticket.id)

    return ticket
