from django import forms
from django.core.exceptions import ValidationError

from .models import CareerApplication, QuoteRequest


class QuoteRequestForm(forms.ModelForm):
    property_type = forms.ChoiceField(
        choices=QuoteRequest.PROPERTY_TYPE_CHOICES,
        initial="residential",
        widget=forms.RadioSelect,
    )
    residential_checklist = forms.MultipleChoiceField(
        choices=QuoteRequest.RESIDENTIAL_CHECKLIST_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
    commercial_checklist = forms.MultipleChoiceField(
        choices=QuoteRequest.COMMERCIAL_CHECKLIST_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
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
            "property_type",
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

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("property_type") == "commercial":
            cleaned_data["selected_checklist"] = cleaned_data.get("commercial_checklist", [])
        else:
            cleaned_data["selected_checklist"] = cleaned_data.get("residential_checklist", [])
        return cleaned_data

    def save(self, commit=True):
        quote = super().save(commit=False)
        quote.checklist_items = self.cleaned_data.get("selected_checklist", [])
        if commit:
            quote.save()
        return quote


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
