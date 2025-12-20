from django.test import TestCase , override_settings
from ..tasks import send_email_staff
from ..models import User


@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class SendEmailStaffTaskTest(TestCase):

     def test_task_run_succesfully(self):
          user = User.objects.create_staff(
               email='ahmed.gaber4371@gmail.com',
               full_name='admin',
               password='StrongPassword'
          )

          result = send_email_staff(user.id)

          self.assertTrue(User.objects.filter(user.id).exists())