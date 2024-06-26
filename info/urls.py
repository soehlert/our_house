from django.urls import path

from .views import ApplianceCreateView
from .views import ApplianceDeleteView
from .views import ApplianceDetailView
from .views import ApplianceListView
from .views import ApplianceUpdateView
from .views import CircuitCreateView
from .views import CircuitDeleteView
from .views import CircuitDetailView
from .views import CircuitDiagramCreateView
from .views import CircuitDiagramDeleteView
from .views import CircuitDiagramUpdateView
from .views import CircuitListView
from .views import CircuitUpdateView
from .views import PaintColorCreateView
from .views import PaintColorDeleteView
from .views import PaintColorDetailView
from .views import PaintColorListView
from .views import PaintColorUpdateView
from .views import RoomCreateView
from .views import RoomUpdateView

urlpatterns = [
    # Appliance URLs
    path("appliances/", ApplianceListView.as_view(), name="appliance_list"),
    path("appliance/<int:pk>/", ApplianceDetailView.as_view(), name="appliance_detail"),
    path("appliance/create/", ApplianceCreateView.as_view(), name="appliance_create"),
    path(
        "appliance/<int:pk>/update/",
        ApplianceUpdateView.as_view(),
        name="appliance_update",
    ),
    path(
        "appliance/<int:pk>/delete/",
        ApplianceDeleteView.as_view(),
        name="appliance_delete",
    ),
    # PaintColor URLs
    path("paintcolors/", PaintColorListView.as_view(), name="paintcolor_list"),
    path(
        "paintcolor/<int:pk>/",
        PaintColorDetailView.as_view(),
        name="paintcolor_detail",
    ),
    path(
        "paintcolor/create/",
        PaintColorCreateView.as_view(),
        name="paintcolor_create",
    ),
    path(
        "paintcolor/<int:pk>/update/",
        PaintColorUpdateView.as_view(),
        name="paintcolor_update",
    ),
    path(
        "paintcolor/<int:pk>/delete/",
        PaintColorDeleteView.as_view(),
        name="paintcolor_delete",
    ),
    # Circuit URLs
    path("circuits/", CircuitListView.as_view(), name="circuit_list"),
    path("circuits/<int:pk>/", CircuitDetailView.as_view(), name="circuit_detail"),
    path("circuits/create/", CircuitCreateView.as_view(), name="circuit_create"),
    path(
        "circuits/<int:pk>/update/",
        CircuitUpdateView.as_view(),
        name="circuit_update",
    ),
    path(
        "circuits/<int:pk>/delete/",
        CircuitDeleteView.as_view(),
        name="circuit_delete",
    ),
    # Room URLs
    path("room/create/", RoomCreateView.as_view(), name="room_create"),
    path("room/<int:pk>/update/", RoomUpdateView.as_view(), name="room_update"),
    # CircuitDiagram URLs
    path(
        "circuitdiagram/create/",
        CircuitDiagramCreateView.as_view(),
        name="circuitdiagram_create",
    ),
    path(
        "circuitdiagram/<int:pk>/update/",
        CircuitDiagramUpdateView.as_view(),
        name="circuitdiagram_update",
    ),
    path(
        "circuitdiagram/<int:pk>/delete/",
        CircuitDiagramDeleteView.as_view(),
        name="circuitdiagram_delete",
    ),
]
