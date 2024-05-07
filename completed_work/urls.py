from django.urls import path, include
from rest_framework import routers

from completed_work.views import CompletedWorkViewSet, complete_work

router = routers.SimpleRouter()
router.register(r'', CompletedWorkViewSet)

urlpatterns = [
    path('', complete_work),
    path('api/', include(router.urls))
]
