from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_email_staff 
from .models import User



@receiver(post_save,sender=User)
def notify_staff_password_setup(sender,instance,created,**kwargs):
     if not created:
          return 
     send_email_staff(instance.id)
