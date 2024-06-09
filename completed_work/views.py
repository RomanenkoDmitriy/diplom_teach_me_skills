from django.shortcuts import render, redirect
from rest_framework.viewsets import ReadOnlyModelViewSet

from completed_work.forms import CommentsWorkForm
# from django.views.generic import

from completed_work.models import CompletedWork, CommentsWork
from completed_work.serializers import CompletedWorkSerializer

import requests as req


class CompletedWorkViewSet(ReadOnlyModelViewSet):
    queryset = CompletedWork.objects.all()
    serializer_class = CompletedWorkSerializer


def complete_work(request):
    response = list(CompletedWork.objects.all())
    if request.user.is_authenticated:
        user = request.user
    else:
        user = False
    return render(request, 'comp_work.html', {'response': response, 'user': user})


def completed_work_detail(request, pk):
    completed_work = CompletedWork.objects.prefetch_related('fotowork_set').get(pk=pk)
    foto = completed_work.fotowork_set.all()
    comments = completed_work.comments.all()
    form = CommentsWorkForm(request.POST)

    response = {
        'completed_work': completed_work,
        'description': completed_work.description,
        'overall_plan': completed_work.overall_plan,
        'all_foto': list(foto),
        'all_comments': list(comments),
        'form_comment': form
    }
    if request.method == 'POST':

        if form.is_valid():
            data = form.cleaned_data
            comment = CommentsWork(user=request.user, comment=data['comment'], completed_work=completed_work)
            comment.save()
            return redirect('detail', pk=pk)

    else:
        return render(request, 'detail_work.html', response)


