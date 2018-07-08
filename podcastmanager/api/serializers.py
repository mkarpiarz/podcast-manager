from rest_framework import serializers
from .models import Podcast

class PodcastSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Podcast
        fields = ('id', 'name', 'url', 'date_added', 'date_updated')
        read_only_fields = ('date_added', 'date_updated')
