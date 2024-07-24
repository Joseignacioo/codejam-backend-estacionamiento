from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('CrearReservacion', CreateReservacionViewset)
router.register('CrearReportes', CreateReportesViewset)
router.register('CrearUsuarios', CreateUsuarioViewSet)
router.register('CrearEstacionamiento', CreateEstacionamientoViewSet)

urlpatterns = [
       path('api/', include(router.urls)),
]