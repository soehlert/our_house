from rest_framework import serializers
from ..models import Appliance, Room, PaintColor, Circuit, CircuitDiagram


class ApplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appliance
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class PaintColorSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)

    class Meta:
        model = PaintColor
        fields = '__all__'


class CircuitDiagramSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircuitDiagram
        fields = '__all__'


class CircuitSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)
    diagrams = CircuitDiagramSerializer(many=True, read_only=True)

    class Meta:
        model = Circuit
        fields = '__all__'
