from cloudinary.models import CloudinaryField
from django.core.validators import FileExtensionValidator
from django.db import models


class QuoteRequest(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ("residential", "Home / Residential"),
        ("commercial", "Business / Commercial"),
    ]

    SERVICE_CHOICES = [
        ("residential", "Residential Cleaning"),
        ("commercial", "Commercial Cleaning"),
        ("deep", "Deep Cleaning"),
        ("move", "Move-In / Move-Out"),
        ("custom", "Custom Request"),
    ]

    RESIDENTIAL_CHECKLIST_CHOICES = [
        ("kitchen", "Kitchen: counters, sink, stovetop, and appliance exteriors"),
        ("bathrooms", "Bathrooms: toilets, tubs/showers, sinks, mirrors, and fixtures"),
        ("bedrooms", "Bedrooms"),
        ("living_areas", "Living room and common areas"),
        ("dusting", "Dusting of reachable surfaces"),
        ("floors", "Vacuuming and mopping floors"),
        ("interior_glass", "Interior windows and glass doors"),
        ("laundry", "Laundry room"),
        ("deep_clean", "Deep cleaning / detail work"),
        ("move_clean", "Move-in or move-out cleaning"),
    ]

    COMMERCIAL_CHECKLIST_CHOICES = [
        ("lobby", "Lobby, entrance, and common areas"),
        ("offices", "Offices and workstations"),
        ("conference", "Conference rooms"),
        ("break_room", "Break room or kitchen"),
        ("restrooms", "Restrooms"),
        ("carpet", "Carpet vacuuming"),
        ("hard_floors", "Hard-floor sweeping and mopping"),
        ("glass", "Interior glass and entry doors"),
        ("trash", "Trash and recycling removal"),
        ("high_touch", "High-touch surface sanitizing"),
        ("supplies", "Restroom supply restocking"),
    ]

    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, default="residential")
    service_type = models.CharField(max_length=30, choices=SERVICE_CHOICES)
    address = models.CharField(max_length=255)
    preferred_date = models.DateField(null=True, blank=True)
    message = models.TextField(blank=True)
    checklist_items = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.get_service_type_display()}"

    def checklist_display(self):
        labels = dict(self.RESIDENTIAL_CHECKLIST_CHOICES + self.COMMERCIAL_CHECKLIST_CHOICES)
        return ", ".join(labels.get(item, item) for item in self.checklist_items) or "No checklist items selected"


class CareerApplication(models.Model):
    POSITION_CHOICES = [
        ("residential_cleaner", "Residential Cleaner"),
        ("commercial_cleaner", "Commercial Cleaner"),
        ("team_lead", "Team Lead"),
        ("flex_position", "Flexible / Any Open Position"),
    ]

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    position = models.CharField(max_length=40, choices=POSITION_CHOICES)
    previous_experience = models.TextField(blank=True)
    motivation = models.TextField()
    flexible_hours = models.BooleanField(default=False)
    resume = CloudinaryField(
        "resume",
        resource_type="raw",
        type="private",
        folder="c2c/resumes",
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "doc", "docx"])],
        help_text="Optional. PDF, DOC, or DOCX; maximum 5 MB.",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_position_display()}"


class GallerySession(models.Model):
    """A published before-and-after pair from a completed cleaning session."""

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    before_image = CloudinaryField("image", folder="c2c/gallery/before")
    after_image = CloudinaryField("image", folder="c2c/gallery/after")
    display_order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "-created_at"]
        verbose_name = "gallery session"
        verbose_name_plural = "gallery sessions"

    def __str__(self):
        return self.title
