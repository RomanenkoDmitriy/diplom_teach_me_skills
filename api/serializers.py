from rest_framework import serializers

from completed_work.models import CompletedWork, CommentsWork, FotoWork
from blueprint.models import Blueprint


class FotoWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoWork
        fields = ['file']


class CompletedWorkSerializer(serializers.ModelSerializer):


    class Meta:
        model = CompletedWork
        fields = ['title', 'description', 'overall_plan']


class CommentsWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsWork
        fields = ['comment', 'completed_work']


class BlueprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blueprint
        fields = ['title',  'file_pdf', 'file_dwg', 'file_b3d']

