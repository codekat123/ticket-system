from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import notify_staff
from .models import Event

@receiver(post_save,sender=Event)
def notify_staff_event(sender,instance,created,**kwargs):
     if not created:
          return
     
     notify_staff(event_id=instance.id)