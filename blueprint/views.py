# from django.shortcuts import render
from django.http import FileResponse
import os
from config.settings import MEDIA_ROOT


from blueprint.models import Blueprint
# from completed_work.models import CompletedWork


def pdf_upload(request, pk):
    obj = Blueprint.objects.get(comp_work_id=pk)
    file_pdf = obj.file_pdf

    return FileResponse(file_pdf, as_attachment=True)


def file_upload(request, pk):
    obj = Blueprint.objects.get(comp_work_id=pk)
    file = obj.file

    return FileResponse(file, as_attachment=True)
