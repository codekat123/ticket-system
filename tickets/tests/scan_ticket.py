from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.urls import reverse
from ..models import Ticket
from events.models import Event
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

class TicketScanTest(APITestCase):

     def setUp(self):
          self.user = (
               User.objects
               .create_superuser(
                    email='Ahmed@gmail.com',
                    full_name='Ahmed Gaber'
               )
          )
          refresh = RefreshToken.for_user(self.user)
          self.client.credentials(
              HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}'
          )
     
     def test_scan_ticket(self):
          event = Event.objects.create(
               title='programming event',
               description='test123',
               location='test123',
               start_date= timezone.now() + timedelta(days=2),
               end_date= timezone.now() + timedelta(days=3),
               capacity=500,
               created_by=self.user
          )

          ticket = Ticket.objects.create(
          email='test@example.com',
          event=event,
          is_used=False,
          used_at=None
          )
          url = reverse('tickets:scan',args=[ticket.qr_code])

          response = self.client.post(url)

          self.assertEqual(status.HTTP_200_OK,response.status_code)