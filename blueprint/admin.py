from django.contrib import admin
from django.http import FileResponse, HttpResponse

from blueprint.models import Blueprint


@admin.register(Blueprint)
class BlueprintAdmin(admin.ModelAdmin):
    list_display = ['file_pdf', 'file', 'comp_work', 'created_at', 'changed_at']
    actions = ['download_file']

    def download_file(self, request, queryset):
        for obj in queryset:
            if obj.file:
                return FileResponse(obj.file, as_attachment=True, filename=obj.file.name)
        return HttpResponse('Ни один файл не выбран')
    download_file.short_description = 'Скачать выбранные файлы'
