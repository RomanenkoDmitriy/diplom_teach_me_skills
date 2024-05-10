from django.contrib import admin

from completed_work.models import CompletedWork, FotoWork, CommentsWork


@admin.register(CompletedWork)
class CompletedWorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'overall_plan', 'created_at', 'updated_at']


@admin.register(FotoWork)
class FotoWorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'completed_work', 'created_at', 'updated_at']


@admin.register(CommentsWork)
class CommentsWorkAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment', 'completed_work', 'created_at', 'updated_at']
