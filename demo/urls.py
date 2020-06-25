from django.urls import path, include
from . import views
from rest_framework import routers
from .views import UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
