from celery import shared_task
from ..models import Event
from django.utils import timezone


@shared_task
def deactivate_finished_events():
    Event.objects.filter(
        end_date__lt=timezone.now(),
        is_active=True
    ).update(is_active=False)
