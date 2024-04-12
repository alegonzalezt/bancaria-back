from django.urls import path, include
from apps.productos.urls import router as productos_router
from apps.usuarios.urls import router as usuarios_router

drf_urls = [
    path('prod/', include(productos_router.urls)),
    path('user/', include(usuarios_router.urls)),
]