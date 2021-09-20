from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Post

# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     body = serializers.CharField()
#
#     def create(self, validated_data):
#         return Post.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.body = validated_data.get('description', instance.body)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body']