from django.contrib import admin

from .models import Appliance
from .models import Circuit
from .models import CircuitDiagram
from .models import PaintColor
from .models import Room


@admin.register(Appliance)
class ApplianceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "model_number",
        "serial_number",
        "appliance_type",
        "purchase_date",
    )
    search_fields = ("name", "model_number", "serial_number", "appliance_type")
    list_filter = ("appliance_type", "purchase_date")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(PaintColor)
class PaintColorAdmin(admin.ModelAdmin):
    list_display = ("paint_code", "paint_color", "paint_base", "purchase_date")
    search_fields = ("paint_code", "paint_color", "paint_base", "room__name")
    list_filter = ("paint_base", "purchase_date")


@admin.register(Circuit)
class CircuitAdmin(admin.ModelAdmin):
    list_display = (
        "circuit_number",
        "description",
        "breaker_size",
        "gfci",
        "afci",
        "cafi",
        "pole_type",
    )
    search_fields = (
        "circuit_number",
        "description",
        "breaker_size",
        "pole_type",
        "rooms__name",
    )
    list_filter = ("breaker_size", "gfci", "afci", "cafi", "pole_type")


@admin.register(CircuitDiagram)
class CircuitDiagramAdmin(admin.ModelAdmin):
    list_display = ("image", "description")
    search_fields = ("description",)
