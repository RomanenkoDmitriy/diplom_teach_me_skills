
from django.urls import path, include
from rest_framework import routers

from completed_work.views import CompletedWorkViewSet, complete_work, completed_work_detail

router = routers.SimpleRouter()
router.register(r'', CompletedWorkViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('detail/<int:pk>/', completed_work_detail, name='detail'),
]



