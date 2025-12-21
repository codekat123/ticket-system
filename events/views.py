from rest_framework.viewsets import ModelViewSet
from .models import Event
from .serializers import EventSerializer
from users.permissions import IsAdmin


class EventView(ModelViewSet):
     queryset = Event.objects.all()
     serializer_class = EventSerializer
     permission_classes = [IsAdmin]