from django.urls import path

from blueprint.views import pdf_upload, dwg_upload, b3d_upload


urlpatterns = [
    path('pdf/<int:pk>/', pdf_upload, name='pdf'),
    path('dwg/<int:pk>/', dwg_upload, name='file_dwg'),
    path('b3d/<int:pk>/', b3d_upload, name='file_b3d'),

]