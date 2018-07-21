from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User

from mptt.models import MPTTModel, TreeForeignKey

from comments.signals import render_markdown
from mortymart.models.abstract import Timestamped
from universe.models import Artifact


class Comment(Timestamped, MPTTModel):
    """
    User comments stored as a modifiable tree (allowing nested comments).
    """

    morty = models.ForeignKey(User, on_delete=models.CASCADE)
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE,
                                 db_index=True)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True,
                            related_name='children')

    content = models.TextField()
    content_html = models.TextField(null=True)

    class MPTTMeta:
        order_insertion_by = ['created_on']


signals.pre_save.connect(render_markdown, sender=Comment)
