from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model
from events.models import Event

User = get_user_model()


class Ticket(models.Model):
    email = models.EmailField(max_length=50)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='tickets'
    )
    qr_code = models.UUIDField(default=uuid4, unique=True)
    is_used = models.BooleanField(default=False)
    used_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'event'],
                name='unique_ticket_per_email_event'
            )
        ]

    def __str__(self):
        return f"{self.email} - {self.event}"
