from django.db import models


class QuoteRequest(models.Model):
    SERVICE_CHOICES = [
        ("residential", "Residential Cleaning"),
        ("commercial", "Commercial Cleaning"),
        ("deep", "Deep Cleaning"),
        ("move", "Move-In / Move-Out"),
        ("custom", "Custom Request"),
    ]

    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    service_type = models.CharField(max_length=30, choices=SERVICE_CHOICES)
    address = models.CharField(max_length=255)
    preferred_date = models.DateField(null=True, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.get_service_type_display()}"


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
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_position_display()}"
