from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from todo.api.resources import TodoViewSet

router = SimpleRouter()
router.register(r'todos', viewset=TodoViewSet)

ApiUrlpatterns = [
    url(r'', include(router.urls)),
]
