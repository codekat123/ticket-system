from rest_framework.test import APITestCase
from django.urls import reverse
from django.test import override_settings 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from ..models import User



class RegisterTest(APITestCase):

     def setUp(self):
          user = User.objects.create_superuser(
               email='ahmed.gaber71@gmail.com',
               full_name='Ahmed Gaber',
               password='testpass123'
          )
          
          refresh = RefreshToken.for_user(user)
          self.client.credentials(
              HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}'
          )
     
     def test_register(self):
          url = reverse('users:register')
          payload = {
               'full_name':'somebody',
               'email':'ahmed.gaber4371@gmail.com',
               'role':'staff'
          }
          response = self.client.post(url,payload,format='json')
          print(response.data)
          self.assertEqual(status.HTTP_201_CREATED,response.status_code)