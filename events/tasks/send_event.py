from celery import shared_task
from django.contrib.auth import get_user_model
from ..models import Event
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings

User = get_user_model()

@shared_task(bind=True, max_retries=3)
def notify_staff(self, event_id):
    try:
        event = Event.objects.filter(id=event_id).first()
        if not event:
            return

        staff_emails = User.objects.filter(
            is_staff=True,
            is_active=True
        ).values_list('email', flat=True)

        if not staff_emails:
            return

        url = reverse('tickets:book', kwargs={'id': event.id})

        context = {
            'title': event.title,
            'start_date': event.start_date,
            'end_date': event.end_date,
            'description': event.description,
            'created_by': event.created_by,
            'url': url,
        }

        html_content = render_to_string(
            'emails/send_event_staff.html',
            context
        )

        email = EmailMultiAlternatives(
            subject=f"New Event: {event.title}",
            body="A new event has been created.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=list(staff_emails),
        )
        email.attach_alternative(html_content, 'text/html')
        email.send()

    except Exception as e:
        raise self.retry(exc=e, countdown=60)
