from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    posted = serializers.DateTimeField()
    title = serializers.CharField(required=True, max_length=128)
    body = serializers.CharField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.posted = validated_data.get('posted', instance.posted)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance