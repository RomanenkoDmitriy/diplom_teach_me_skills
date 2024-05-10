from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from completed_work.models import CompletedWork, FotoWork
from completed_work.serializers import CompletedWorkSerializer


class CompletedWorkViewSet(ReadOnlyModelViewSet):
    queryset = CompletedWork.objects.all()
    serializer_class = CompletedWorkSerializer


def complete_work(request):
    response = list(CompletedWork.objects.all())
    return render(request, 'comp_work.html', {'response': response})


def completed_work_detail(request, pk):
    completed_work = CompletedWork.objects.prefetch_related('fotowork_set').get(pk=pk)
    foto = completed_work.fotowork_set.all()
    # print(completed_work, foto.all())
    response = {
        'title': completed_work.title,
        'description': completed_work.description,
        'overall_plan': completed_work.overall_plan,
        'all_foto': list(foto)
    }

    return render(request, 'detail_work.html', {'response': response})
