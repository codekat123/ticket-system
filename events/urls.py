from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
     EventView,
     AdminEventDetailView
)


app_name = 'events'

router = DefaultRouter()

router.register(r'',EventView,basename='event')

urlpatterns = [
     path('get-info/<int:id>/',AdminEventDetailView.as_view(),name='get-info')
]

urlpatterns += router.urls