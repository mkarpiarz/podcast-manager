from django.shortcuts import render
from .models import Podcast
from .serializers import PodcastSerializer
from rest_framework import views, response, status

class PodcastList(views.APIView):
    """List all snippets, or create a new snippet."""

    def get(self, request, format=None):
        podcasts = Podcast.objects.all()
        serializer = PodcastSerializer(podcasts, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PodcastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
