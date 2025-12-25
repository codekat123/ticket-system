from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.urls import reverse
from django.test import override_settings
from .models import Event
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta


User = get_user_model()

class EventTest(APITestCase):

     def setUp(self):
          user = User.objects.create_superuser(
               full_name='Ahmed Gaber',
               email='ahmed@gmail.com'
          )

          self.event = (
               Event.objects.create(
               title='programming event',
               description='test123',
               location='test123',
               start_date= timezone.now() + timedelta(days=2),
               end_date= timezone.now() + timedelta(days=3),
               capacity=500,
               created_by=user
               )
          )
          refresh = RefreshToken.for_user(user)
          self.client.credentials(
              HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}'
          )

     def test_get_event_info(self):
          url = reverse("events:get-info",kwargs={'event_id':self.event.id})

          response = self.client.get(url)
          print(response.data)
          self.assertEqual(status.HTTP_200_OK,response.status_code)