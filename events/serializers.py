from rest_framework import serializers
from django.utils import timezone
from .models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'location',
            'start_date',
            'end_date',
            'capacity'
        ]

    def validate(self, data):
        now = timezone.now()
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        errors = {}
        
        if start_date < now:
            errors['start_date'] = 'Start date cannot be in the past.'
        
        if end_date < now:
            errors['end_date'] = 'End date cannot be in the past.'
        
        if start_date >= end_date:
            errors['end_date'] = 'End date must be after start date.'
        
        if errors:
            raise serializers.ValidationError(errors)


        return data
