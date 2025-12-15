from rest_framework.routers import DefaultRouter
from .views import NominaViewSet

router = DefaultRouter()
router.register(r'nominas', NominaViewSet)

urlpatterns = router.urls