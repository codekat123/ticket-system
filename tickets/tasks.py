from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import generate_qr_image
from .models import Ticket

@shared_task
def send_ticket_email(ticket_id):
    ticket = Ticket.objects.filter(id=ticket_id).first()
    if not ticket:
        return
    
    subject = f"Your ticket for {ticket.event.title}"
    body = f"""
Hi,

Here is your ticket for:
{ticket.event.title}

Please show the attached QR code at the entrance.
"""

    email = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[ticket.email],
    )

    qr_image = generate_qr_image(str(ticket.qr_code))
    email.attach("ticket_qr.png", qr_image.read(), "image/png")

    email.send()
