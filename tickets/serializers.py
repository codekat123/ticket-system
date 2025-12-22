from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
     class Meta:
          model = Ticket
          fields = ['email']
     
     def validate(self,attrs):
          event = self.context['event']
          email = attrs['email']

          if Ticket.objects.filter(event=event,email=email).exists():
               raise serializers.ValidationError(
                    "you already have a ticket for this event"
               )
          
          return attrs
     