from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics, mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from rest.models import Post
from rest.serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView

def Index(request):
    return HttpResponse("Hello World")

'''
# Function Based API View
@csrf_exempt
def post_list(request):
    # get all posts
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def post_details(request, pk):
    try:
        post = Post.objects.get(pk=pk)

    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)
'''

'''
# Decorators
@api_view(['GET', 'POST'])
def post_list(request):
    # get all posts
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def post_details(request, pk):
    try:
        post = Post.objects.get(pk=pk)

    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

'''
# Class APIView
class PostList(APIView):
    def get(self, request):
        posts=Post.objects.all()
        serilizer = PostSerializer(posts, many=True)
        return Response(serilizer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetails(APIView):
    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        post = self.get_object(id)
        serilizer = PostSerializer(post)
        return Response(serilizer.data)

    def put(self, request, id):
        post = self.get_object(id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

'''
# mixins
class PostList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class PostDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)
'''

'''
# ViewSet
class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        post = Post.objects.get(pk = pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        post = Post.objects.get(pk = pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

'''
# GenericViewSet
class PostViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer