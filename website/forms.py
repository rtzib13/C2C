from django import forms

from .models import CareerApplication, QuoteRequest


class QuoteRequestForm(forms.ModelForm):
    preferred_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
        help_text="Optional",
    )

    class Meta:
        model = QuoteRequest
        fields = [
            "full_name",
            "email",
            "phone",
            "service_type",
            "address",
            "preferred_date",
            "message",
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "(662) 308-5118"}),
            "address": forms.TextInput(attrs={"placeholder": "Service address"}),
            "message": forms.Textarea(attrs={"rows": 5, "placeholder": "Tell us what you need cleaned"}),
        }


class CareerApplicationForm(forms.ModelForm):
    class Meta:
        model = CareerApplication
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "position",
            "previous_experience",
            "motivation",
            "flexible_hours",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "(662) 308-5118"}),
            "previous_experience": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Describe your cleaning experience"}
            ),
            "motivation": forms.Textarea(attrs={"rows": 4, "placeholder": "Why do you want to join our team?"}),
        }
