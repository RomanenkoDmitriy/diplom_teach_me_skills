from django.contrib import admin
from django.http import FileResponse, HttpResponse

from blueprint.models import Blueprint


@admin.register(Blueprint)
class BlueprintAdmin(admin.ModelAdmin):
    list_display = ['title', 'file_pdf', 'file_dwg', 'file_b3d', 'comp_work', 'created_at', 'changed_at']
