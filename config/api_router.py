from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from our_house.users.api.views import UserViewSet
from info.api.views import (
    ApplianceViewSet, RoomViewSet, PaintColorViewSet, CircuitViewSet, CircuitDiagramViewSet
)

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('users', UserViewSet)
router.register('appliances', ApplianceViewSet)
router.register('rooms', RoomViewSet)
router.register('paintcolors', PaintColorViewSet)
router.register('circuits', CircuitViewSet)
router.register('circuit-diagrams', CircuitDiagramViewSet)

# Export the router's URLs for inclusion in the main URL configuration
app_name = "api"
urlpatterns = router.urls

