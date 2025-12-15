from rest_framework import routers
from .views_api import (
    EmpleadoViewSet, DepartamentoViewSet, PuestoViewSet, ContratoViewSet,
    AsistenciaViewSet, VacacionViewSet, NominaViewSet, EvaluacionViewSet,
    BeneficioViewSet, BeneficioEmpleadoViewSet
)

router = routers.DefaultRouter()

router.register(r'empleados', EmpleadoViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'puestos', PuestoViewSet)
router.register(r'contratos', ContratoViewSet)
router.register(r'asistencias', AsistenciaViewSet)
router.register(r'vacaciones', VacacionViewSet)
router.register(r'nominas', NominaViewSet)
router.register(r'evaluaciones', EvaluacionViewSet)
router.register(r'beneficios', BeneficioViewSet)
router.register(r'beneficios-empleados', BeneficioEmpleadoViewSet)

urlpatterns = router.urls
