from django.urls import path
from .views import EventView
from rest_framework.routers import DefaultRouter


app_name = 'events'

router = DefaultRouter()

router.register(r'',EventView,basename='event')

urlpatterns = router.urls