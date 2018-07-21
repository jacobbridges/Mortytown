from django.db import models


class Reality(models.Model):
    """
    An infinite number of alternate realities where Mortys could exist.
    (A site with comments.)
    """

    domain = models.CharField(max_length=100)
    # ..maybe registration in the future?

    total_comments = models.PositiveIntegerField(default=0)
    total_mortys = models.PositiveIntegerField(default=0)

    # Properties -------------------------------------------------------------

    @property
    def total_users(self):
        """Alias to total_mortys field."""
        return self.total_mortys
