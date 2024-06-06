from django import forms
from django_addanother.widgets import AddAnotherWidgetWrapper
from django.urls import reverse_lazy
from .models import Appliance, PaintColor, Circuit, Room, CircuitDiagram


class ApplianceForm(forms.ModelForm):
    class Meta:
        model = Appliance
        fields = [
            'name', 'model_number', 'serial_number', 'appliance_type', 'receipt',
            'owners_manual', 'image', 'purchase_location', 'registered', 'purchase_date',
            'power_demands', 'notes'
        ]
        widgets = {
            'appliance_type': forms.Select(attrs={'class': 'form-control'}),
            'purchase_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class PaintColorForm(forms.ModelForm):
    class Meta:
        model = PaintColor
        fields = ['room', 'paint_code', 'paint_color', 'paint_base', 'purchase_date']
        widgets = {
            'room': AddAnotherWidgetWrapper(
                forms.SelectMultiple(attrs={'class': 'form-control wide-select'}),
                reverse_lazy('room_create')
            ),
            'purchase_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class CircuitForm(forms.ModelForm):
    class Meta:
        model = Circuit
        fields = [
            'rooms', 'circuit_number', 'description', 'breaker_size', 'gfci', 'afci', 'cafi',
            'pole_type', 'diagrams'
        ]
        labels = {
            'gfci': 'GFCI',
            'afci': 'AFCI',
            'cafi': 'CAFI',
        }
        widgets = {
            'pole_type': forms.Select(attrs={'class': 'form-control'}),
            'breaker_size': forms.Select(attrs={'class': 'form-control'}),
            'rooms': AddAnotherWidgetWrapper(
                forms.SelectMultiple(attrs={'class': 'form-control wide-select'}),
                reverse_lazy('room_create')
            ),
            'diagrams': AddAnotherWidgetWrapper(
                forms.SelectMultiple(attrs={'class': 'form-control wide-select'}),
                reverse_lazy('circuitdiagram_create')
            ),
        }


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']


class CircuitDiagramForm(forms.ModelForm):
    class Meta:
        model = CircuitDiagram
        fields = ['image', 'description']
