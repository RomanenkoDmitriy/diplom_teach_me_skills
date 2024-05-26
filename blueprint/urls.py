from django.urls import path

from blueprint.views import pdf_upload, file_upload


urlpatterns = [
    path('pdf/<int:pk>/', pdf_upload, name='pdf'),
    path('file/<int:pk>/', file_upload, name='file'),

]