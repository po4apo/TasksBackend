from django.urls import path, include
from django.contrib import admin

from backend.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
