from django.db import models


class Timestamped(models.Model):
    """
    Abstract model providing timestamp fields.
    """

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
