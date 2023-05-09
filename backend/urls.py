from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import TaskViewSet

router = SimpleRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]