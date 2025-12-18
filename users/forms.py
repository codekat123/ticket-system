from django import forms

class SetPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "New password"}),
        min_length=8,
        label="New password",
    )
