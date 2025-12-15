from rest_framework.routers import DefaultRouter
from .views import BeneficioEmpleadoViewSet

router = DefaultRouter()
router.register(r'beneficios-empleados', BeneficioEmpleadoViewSet)

urlpatterns = router.urls