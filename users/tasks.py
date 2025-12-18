from celery import shared_task
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.urls import reverse

User = get_user_model()


@shared_task(bind=True, max_tries=3, default_retry_delay=60)
def send_email_staff(self, pk):
    try:
        user = User.objects.get(id=pk)

        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = default_token_generator.make_token(user)

       
        set_password_path = reverse(
            "staff-set-password",
            kwargs={"uuid": uid, "token": token}
        )



        context = {
            "user": user,
            "set_password_url": set_password_path,
            "current_year": 2025,
        }

        html_content = render_to_string(
            "emails/staff_set_password.html",
            context
        )

        email = EmailMultiAlternatives(
            subject="Set Your Staff Account Password",
            body="Please use an email client that supports HTML.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )

        email.attach_alternative(html_content, "text/html")
        email.send()

    except Exception as exc:
        raise self.retry(exc=exc)



     
