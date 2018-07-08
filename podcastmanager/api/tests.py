from django.test import TestCase
from .models import Podcast
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class PodcastTestCase(TestCase):
    """This class defines the test suite for the Podcast model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.podcast_name = "Serial"
        self.podcast_url = "https://itunes.apple.com/us/podcast/serial/id917918570"
        self.podcast = Podcast(name=self.podcast_name, url=self.podcast_url)

    def test_model_can_create_a_podcast(self):
        """Test the Podcast model can create a podcast."""
        old_count = Podcast.objects.count()
        self.podcast.save()
        new_count = Podcast.objects.count()
        self.assertGreater(new_count, old_count)

class PodcastListTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.podcast_data = {'name': 'Serial', 'url': 'https://itunes.apple.com/us/podcast/serial/id917918570'}

    def test_api_can_create_a_podcast(self):
        """Test the api has podcast creation capability."""
        self.response = self.client.post(
            reverse('list_and_create'),
            self.podcast_data,
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_list_podcasts(self):
        """Test the api can retrieve a list of podcasts."""
        # First, create an item
        self.client.post(
            reverse('list_and_create'),
            self.podcast_data,
            format="json")
        # then try to retrieve it
        self.response = self.client.get(
            reverse('list_and_create'),
            format="json")
        self.assertContains(self.response, self.podcast_data['url'], status_code=status.HTTP_200_OK)
