from django.contrib import admin

from .models import CareerApplication, GallerySession, QuoteRequest


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ("full_name", "service_type", "email", "phone", "created_at")
    list_filter = ("service_type", "created_at")
    search_fields = ("full_name", "email", "phone", "address")


@admin.register(CareerApplication)
class CareerApplicationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "position", "email", "phone", "has_resume", "flexible_hours", "created_at")
    list_filter = ("position", "flexible_hours", "created_at")
    search_fields = ("first_name", "last_name", "email", "phone")

    @admin.display(boolean=True, description="Resume")
    def has_resume(self, obj):
        return bool(obj.resume)


@admin.register(GallerySession)
class GallerySessionAdmin(admin.ModelAdmin):
    list_display = ("title", "display_order", "is_published", "created_at")
    list_editable = ("display_order", "is_published")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "description")
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Session details", {"fields": ("title", "description", "display_order", "is_published")} ),
        ("Before and after photos", {"fields": ("before_image", "after_image")} ),
        ("Record", {"fields": ("created_at",)}),
    )
