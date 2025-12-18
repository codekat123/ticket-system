from django.urls import path
from .views import (
     RegisterCreateAPIView,
     LogoutAPIView,
     staff_set_password_view
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name='users'

urlpatterns = [
     path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

     path('register/',RegisterCreateAPIView.as_view(),name='register'),
     path('logout/',LogoutAPIView.as_view(),name='logout'),

     path('set_password/<uuid>/<token>/',staff_set_password_view,name='staff-set-password')

     
]