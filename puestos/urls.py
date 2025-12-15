from rest_framework.routers import DefaultRouter
from .views import PuestoViewSet

router = DefaultRouter()
router.register(r'puestos', PuestoViewSet)

urlpatterns = router.urls