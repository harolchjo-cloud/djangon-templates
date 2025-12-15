from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Serve decorated API index at /api/
    path('api/', TemplateView.as_view(template_name='api/index.html'), name='api-index'),
    # Grouped API endpoints
    # api1: core employee/position/department endpoints
    path('api/api1/', include('departamentos.urls')),
    path('api/api1/', include('puestos.urls')),
    path('api/api1/', include('empleados.urls')),
    # Aliases for decorated docs links
    path('api/v1/', include('departamentos.urls')),
    path('api/v1/', include('puestos.urls')),
    path('api/v1/', include('empleados.urls')),

    # api2: contracts, attendances, vacations
    path('api/api2/', include('contratos.urls')),
    path('api/api2/', include('asistencias.urls')),
    path('api/api2/', include('vacaciones.urls')),
    # Aliases for decorated docs links
    path('api/v2/', include('contratos.urls')),
    path('api/v2/', include('asistencias.urls')),
    path('api/v2/', include('vacaciones.urls')),

    # api3: payroll, evaluations and benefits
    path('api/api3/', include('nominas.urls')),
    path('api/api3/', include('evaluaciones.urls')),
    path('api/api3/', include('beneficios.urls')),
    path('api/api3/', include('beneficios_empleados.urls')),
    # Aliases for decorated docs links
    path('api/v3/', include('nominas.urls')),
    path('api/v3/', include('evaluaciones.urls')),
    path('api/v3/', include('beneficios.urls')),
    path('api/v3/', include('beneficios_empleados.urls')),
]

