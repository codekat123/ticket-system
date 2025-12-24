from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from django.test import override_settings
from django.contrib.auth import get_user_model
from events.models import Event
from django.utils import timezone
from datetime import timedelta

User = get_user_model()


class TicketTest(APITestCase):

     def setUp(self):
          self.user = (
               User.objects
               .create_superuser(
                    email='ahmed.gaber4371@gmail.com',
                    full_name='Ahmed Gaber'
               )
          )
          refresh = RefreshToken.for_user(self.user)
          self.client.credentials(
              HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}'
          )
     
     def test_book_ticket(self):
          event = Event.objects.create(
               title='programming event',
               description='test123',
               location='test123',
               start_date= timezone.now() + timedelta(days=2),
               end_date= timezone.now() + timedelta(days=3),
               capacity=500,
               created_by=self.user
          )
          url = reverse('tickets:book',kwargs={'event_id': event.id})

          payload  = {
               'email':'ahmed@gmail.com'
          }

          response = self.client.post(url,payload,format='json')
          self.assertEqual(status.HTTP_201_CREATED,response.status_code)