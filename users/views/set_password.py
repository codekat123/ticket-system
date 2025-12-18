from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.contrib import messages

from ..models import User
from ..forms import SetPasswordForm


def staff_set_password_view(request, uuid, token):
    try:
        user_id = urlsafe_base64_decode(uuid).decode()
        user = User.objects.get(id=user_id)
    except (ValueError, User.DoesNotExist):
        return HttpResponseBadRequest("Invalid or expired link")

    if not (user.is_staff or user.is_superuser):
        return HttpResponseForbidden("Unauthorized")

    if not default_token_generator.check_token(user, token):
        return HttpResponseBadRequest("Invalid or expired token")

    if request.method == "POST":
        form = SetPasswordForm(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data["password"])
            user.is_active = True
            user.save()

            messages.success(
                request,
                "Password set successfully. Your account is now active."
            )
            return render(request,"auth/staff_set_password.html",{'form':form})

    else:
        form = SetPasswordForm()

    return render(
        request,
        "auth/staff_set_password.html",
        {"form": form}
    )
