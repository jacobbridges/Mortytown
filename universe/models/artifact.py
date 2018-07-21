from django.db import models

from mortymart.models import Timestamped
from universe.models.realities import Reality


class Artifact(Timestamped):
    """
    Any dumb thing in any of the infinite realities Mortys find commentable.
    (The abjective context of a comment -- e.g. squad, news article, etc.)
    """

    reality = models.ForeignKey(Reality, on_delete=models.CASCADE)
    path = models.CharField(max_length=2000)
    meta = models.CharField(max_length=500, null=True)

    total_comments = models.PositiveIntegerField(default=0, null=True)
    total_mortys = models.PositiveIntegerField(default=0, null=True)

    # Properties -------------------------------------------------------------

    @property
    def total_users(self):
        """Alias to total_mortys field."""
        return self.total_mortys

    # Methods ----------------------------------------------------------------

    def get_comments(self):
        """Get all comments associated with this artifact."""
        return self.comment_set.all()
