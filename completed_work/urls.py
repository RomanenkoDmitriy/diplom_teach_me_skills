
from django.urls import path, include
from rest_framework import routers

from completed_work.views import complete_work, completed_work_detail

# router = routers.SimpleRouter()
# router.register(r'', CompletedWorkViewSet)

urlpatterns = [
    path('detail/<int:pk>/', completed_work_detail, name='detail'),
]



