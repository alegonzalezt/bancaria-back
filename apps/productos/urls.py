from django.urls import path, include
from rest_framework import routers
from apps.productos.views.cuentas_bancarias import CuentasBancariasViews
from apps.productos.views.transacciones_bancarias import TransaccionesBancariasViews

app_name = 'productos'
router = routers.DefaultRouter()
router.register('cuenta-bancaria', CuentasBancariasViews, basename="cuenta-bancaria")
router.register('transa-bancaria', TransaccionesBancariasViews, basename="transa-bancaria")

urlpatterns = [
    path('', include(router.urls)),
]