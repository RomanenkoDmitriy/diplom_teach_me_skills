from django.http import FileResponse

from blueprint.models import Blueprint


def pdf_upload(request, pk):
    obj = Blueprint.objects.get(comp_work_id=pk)
    file_pdf = obj.file_pdf

    return FileResponse(file_pdf, as_attachment=True)


def file_upload(request, pk):
    obj = Blueprint.objects.get(comp_work_id=pk)
    file = obj.file

    return FileResponse(file, as_attachment=True)
