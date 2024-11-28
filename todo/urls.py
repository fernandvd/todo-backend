from django.urls import include, path 

from rest_framework.routers import DefaultRouter

from .views import TodoViewSet

router = DefaultRouter()
router.register('todo', TodoViewSet)

app_name='todo'

urlpatterns = [
    path('', include(router.urls)),
]