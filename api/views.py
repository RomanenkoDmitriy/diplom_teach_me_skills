from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import CompletedWorkSerializer, CommentsWorkSerializer, BlueprintSerializer
from blueprint.models import Blueprint
from completed_work.models import CommentsWork, CompletedWork


class CompletedWorkViewSet(ReadOnlyModelViewSet):
    queryset = CompletedWork.objects.all()
    serializer_class = CompletedWorkSerializer


class CommentsWorkViewSet(APIView):
    permission_classes = ()

    def get(self, request, pk):
        comments = CommentsWorkSerializer(CommentsWork.objects.filter(completed_work=pk), many=True)

        return Response(comments.data)

    def post(self, request):
        serializer = CommentsWorkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class BlueprintViewSet(APIView):
    permission_classes = ()

    def get(self, request):
        blueprints = Blueprint.objects.all()
        serializer = BlueprintSerializer(blueprints, many=True)
        return Response(serializer.data)

