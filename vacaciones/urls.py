from rest_framework.routers import DefaultRouter
from .views import VacacionViewSet

router = DefaultRouter()
router.register(r'vacaciones', VacacionViewSet)

urlpatterns = router.urls