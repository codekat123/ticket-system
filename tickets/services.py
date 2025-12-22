from django.db import transaction
from .tasks import send_ticket_email


@transaction.atomic
def create_ticket_and_send_it(serializer,event):
     ticket = serializer.save(event=event)
     send_ticket_email(ticket.id)
     return ticket