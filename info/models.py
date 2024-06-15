from django.db import models


class Appliance(models.Model):
    APPLIANCE_TYPE_CHOICES = [
        ("gas", "Gas"),
        ("electric", "Electric"),
        ("induction", "Induction"),
    ]

    name = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    appliance_type = models.CharField(max_length=10, choices=APPLIANCE_TYPE_CHOICES)
    receipt = models.FileField(upload_to="receipts/", blank=True, null=True)
    owners_manual = models.FileField(upload_to="owners_manuals/", blank=True, null=True)
    specs = models.FileField(upload_to="specs/", blank=True, null=True)
    install_docs = models.FileField(upload_to="install_docs/", blank=True, null=True)
    image = models.ImageField(upload_to="appliance_images/", null=True, blank=True)
    purchase_location = models.CharField(max_length=100)
    registered = models.BooleanField(default=False)
    purchase_date = models.DateField()
    power_demands = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class PaintColor(models.Model):
    room = models.ManyToManyField(Room)
    paint_code = models.CharField(max_length=100)
    paint_color = models.CharField(max_length=100)
    paint_base = models.CharField(max_length=100)
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.paint_color} ({self.paint_code}) in {self.room}"


class CircuitDiagram(models.Model):
    image = models.ImageField(upload_to="circuit_diagrams/")
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description or "Circuit Diagram"


class Circuit(models.Model):
    BREAKER_SIZE_CHOICES = [
        ("15A", "15A"),
        ("20A", "20A"),
        ("30A", "30A"),
        ("40A", "40A"),
        ("50A", "50A"),
    ]

    rooms = models.ManyToManyField(Room, blank=True)
    circuit_number = models.IntegerField()
    description = models.CharField(max_length=255)
    breaker_size = models.CharField(max_length=10, choices=BREAKER_SIZE_CHOICES)
    gfci = models.BooleanField(default=False)
    afci = models.BooleanField(default=False)
    cafi = models.BooleanField(default=False)
    pole_type = models.CharField(
        max_length=10,
        choices=[("single", "Single Pole"), ("double", "Double Pole")],
    )
    diagrams = models.ManyToManyField(CircuitDiagram, blank=True)

    def __str__(self):
        return f"Circuit {self.circuit_number} - {self.description}"
