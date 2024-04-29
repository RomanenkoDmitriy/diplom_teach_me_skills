from rest_framework import serializers

from completed_work.models import CompletedWork, FotoWork, CommentsWork


class CompletedWorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompletedWork
        fields = ['id', 'title', 'description', 'overall_plan', 'created_at', 'updated_at']


class FotoWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoWork
        fields = ['id', 'file', 'created_at', 'updated_at']


class CommentsWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsWork
        fields = ['id', 'user', 'completed_work', 'created_at', 'updated_at']
