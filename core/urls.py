from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('departamentos.urls')),
    path('api/', include('puestos.urls')),
    path('api/', include('empleados.urls')),
    path('api/', include('contratos.urls')),
    path('api/', include('asistencias.urls')),
    path('api/', include('vacaciones.urls')),
    path('api/', include('nominas.urls')),
    path('api/', include('evaluaciones.urls')),
    path('api/', include('beneficios.urls')),
    path('api/', include('beneficios_empleados.urls')),
]

