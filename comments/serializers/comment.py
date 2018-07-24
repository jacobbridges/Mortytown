from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    morty_id = serializers.IntegerField()
    artifact_id = serializers.IntegerField()
    parent_id = serializers.IntegerField()
    content = serializers.TextField()
    content_html = serializers.TextField(required=False, allow_blank=True)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.morty_id = validated_data.get('morty_id', instance.morty_id)
        instance.artifact_id = validated_data.get('artifact_id', instance.artifact_id)
        instance.parent_id = validated_data.get('parent_id', instance.parent_id)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


class EasyCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'morty_id', 'artifact_id', 'parent_id', 'content', 'content_html')

