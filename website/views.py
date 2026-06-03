import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import CareerApplicationForm, QuoteRequestForm

logger = logging.getLogger(__name__)


def _notify_owner(subject, body):
    send_mail(
        subject=subject,
        message=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.CONTACT_NOTIFICATION_EMAIL],
        fail_silently=False,
    )


def home(request):
    return render(
        request,
        "website/home.html",
        {
            "page_title": "Cummings 2 Clean | Premium Cleaning Services",
        },
    )


def about(request):
    return render(request, "website/about.html", {"page_title": "About | Cummings 2 Clean"})


def services(request):
    return render(request, "website/services.html", {"page_title": "Services | Cummings 2 Clean"})


def careers(request):
    if request.method == "POST":
        form = CareerApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            try:
                _notify_owner(
                    subject=f"New Career Application: {application.first_name} {application.last_name}",
                    body=(
                        f"Position: {application.get_position_display()}\n"
                        f"Name: {application.first_name} {application.last_name}\n"
                        f"Email: {application.email}\n"
                        f"Phone: {application.phone}\n"
                        f"Flexible Hours: {'Yes' if application.flexible_hours else 'No'}\n\n"
                        f"Previous Experience:\n{application.previous_experience or 'N/A'}\n\n"
                        f"Motivation:\n{application.motivation}"
                    ),
                )
                messages.success(request, "Application submitted successfully. Our team will review it soon.")
            except Exception as exc:
                logger.exception("Career application email failed: %s", exc)
                messages.warning(
                    request,
                    "Application was saved, but email delivery is not configured yet. Please verify SMTP settings.",
                )
            return redirect("careers")
    else:
        form = CareerApplicationForm()

    return render(
        request,
        "website/careers.html",
        {
            "page_title": "Careers | Cummings 2 Clean",
            "form": form,
        },
    )


def contact(request):
    if request.method == "POST":
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            quote = form.save()
            try:
                _notify_owner(
                    subject=f"New Quote Request: {quote.full_name}",
                    body=(
                        f"Service: {quote.get_service_type_display()}\n"
                        f"Name: {quote.full_name}\n"
                        f"Email: {quote.email}\n"
                        f"Phone: {quote.phone}\n"
                        f"Address: {quote.address}\n"
                        f"Preferred Date: {quote.preferred_date or 'Not provided'}\n\n"
                        f"Message:\n{quote.message or 'N/A'}"
                    ),
                )
                messages.success(request, "Your request has been sent. We will contact you soon.")
            except Exception as exc:
                logger.exception("Quote notification email failed: %s", exc)
                messages.warning(
                    request,
                    "Your request was saved, but email delivery is not configured yet. Please verify SMTP settings.",
                )
            return redirect("contact")
    else:
        form = QuoteRequestForm()

    return render(
        request,
        "website/contact.html",
        {
            "page_title": "Contact | Cummings 2 Clean",
            "form": form,
        },
    )


def application_success(request):
    return render(
        request,
        "website/application_success.html",
        {"page_title": "Thank You | Cummings 2 Clean"},
    )
