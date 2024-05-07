from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from completed_work.models import CompletedWork
from completed_work.serializers import CompletedWorkSerializer


class CompletedWorkViewSet(ReadOnlyModelViewSet):
    queryset = CompletedWork.objects.all()
    serializer_class = CompletedWorkSerializer


def complete_work(request):
    response = list(CompletedWork.objects.all())
    return render(request, 'comp_work.html', {'response': response})
