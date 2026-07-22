from django import forms
from django.core.exceptions import ValidationError

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
    MAX_RESUME_SIZE = 5 * 1024 * 1024

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
            "resume",
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
            "resume": forms.ClearableFileInput(attrs={"accept": ".pdf,.doc,.docx"}),
        }

    def clean_resume(self):
        resume = self.cleaned_data.get("resume")
        if resume and resume.size > self.MAX_RESUME_SIZE:
            raise ValidationError("Please upload a resume smaller than 5 MB.")
        return resume
