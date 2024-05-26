from django.db import models

from completed_work.models import CompletedWork


class Blueprint(models.Model):
    file_pdf = models.FileField(upload_to='blueprints/pdf')
    file = models.FileField(upload_to='blueprints/file')
    comp_work = models.ForeignKey(CompletedWork, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
