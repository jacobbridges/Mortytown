from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from comments.models import Comment
from universe.models import Reality, Artifact


class Command(BaseCommand):
    help = 'Testing comments with a tree structure'

    def handle(self, *args, **options):
        try:
            u = User.objects.get(id=1)
        except:
            u = User.objects.create(username='test', email='test@test.com', password='test')

        try:
            a = Artifact.objects.get(id=1)
        except:
            r = Reality.objects.create(domain='futhead.com')
            a = Artifact.objects.create(
                reality=r,
                path='futhead.com/18/totw/totw38/',
            )

        c = Comment.objects.create(
            morty=u,
            artifact=a,
            content='**Parent**'
        )
        c2 = Comment.objects.create(
            morty=u,
            artifact=a,
            parent=c,
            content='I"m a child!'
        )
        c3 = Comment.objects.create(
            morty=u,
            artifact=a,
            parent=c2,
            content='Deeper child.'
        )

        print(a.get_comments())
