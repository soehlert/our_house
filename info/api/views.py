from rest_framework import viewsets

from ..models import Appliance
from ..models import Circuit
from ..models import CircuitDiagram
from ..models import PaintColor
from ..models import Room
from .serializers import ApplianceSerializer
from .serializers import CircuitDiagramSerializer
from .serializers import CircuitSerializer
from .serializers import PaintColorSerializer
from .serializers import RoomSerializer


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
