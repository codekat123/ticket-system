from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Event(models.Model):
     title = models.CharField(max_length=250)
     description = models.TextField(max_length=500)
     location = models.TextField(max_length=500)
     is_active = models.BooleanField(default=True)
     start_date = models.DateTimeField()
     end_date = models.DateTimeField()
     capacity = models.PositiveIntegerField()
     created_at = models.DateTimeField(auto_now_add=True)
     created_by = models.ForeignKey(User,on_delete=models.CASCADE)

     class Meta:
          indexes = [
               models.Index(
                    fields=['title']
               )
          ]
          constraints = [
            models.UniqueConstraint(
                fields=['date'],
                name='unique_event_date'
            )
        ]