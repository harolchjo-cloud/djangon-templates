from rest_framework.routers import DefaultRouter
from .views import BeneficioViewSet

router = DefaultRouter()
router.register(r'beneficios', BeneficioViewSet)

urlpatterns = router.urls
