from rest_framework import viewsets
from ..models import Appliance, Room, PaintColor, Circuit, CircuitDiagram
from .serializers import (
    ApplianceSerializer, RoomSerializer, PaintColorSerializer, CircuitSerializer, CircuitDiagramSerializer
)


class ApplianceViewSet(viewsets.ModelViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class PaintColorViewSet(viewsets.ModelViewSet):
    queryset = PaintColor.objects.all()
    serializer_class = PaintColorSerializer


class CircuitViewSet(viewsets.ModelViewSet):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer


class CircuitDiagramViewSet(viewsets.ModelViewSet):
    queryset = CircuitDiagram.objects.all()
    serializer_class = CircuitDiagramSerializer
