from django.db import models

class Podcast(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=512, blank=False)
    url = models.CharField(max_length=512, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
