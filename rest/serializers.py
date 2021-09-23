from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.views import Token

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
        fields = ['id', 'author', 'title', 'body']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)

class UserSerilizer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'groups']

        extra_kwargs = {
            'password':{
                'write_only':True,
                'required':True
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.groups.add(1)
        Token.objects.create(user=user)
        return user
