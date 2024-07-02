from django.urls import path
from rest_framework.routers import SimpleRouter

from api.views import CompletedWorkViewSet, CommentsWorkViewSet, BlueprintViewSet

router = SimpleRouter()
router.register('completed_work', CompletedWorkViewSet)

urlpatterns = [
    path('comments/<int:pk>/', CommentsWorkViewSet.as_view()),
    path('blueprint/', BlueprintViewSet.as_view()),
]
urlpatterns += router.urls
