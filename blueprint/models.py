from django.db import models

from completed_work.models import CompletedWork


class Blueprint(models.Model):
    title = models.CharField(max_length=100)
    file_pdf = models.FileField(upload_to='blueprints/pdf', null=True, blank=True)
    file_dwg = models.FileField(upload_to='blueprints/dwg', null=True, blank=True)
    file_b3d = models.FileField(upload_to='blueprints/b3d', null=True, blank=True)
    comp_work = models.ForeignKey(CompletedWork, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-changed_at']
