from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.exceptions import status


from django.shortcuts import get_object_or_404


@api_view()
def index(request):
    return Response("Hello, world. You're at the polls index.")


@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    my_post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        my_data = PostSerializer(my_post)
        return Response(my_data.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(my_post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        my_post.delete()
        return Response({'message':'item delete successfully'},status=status.HTTP_204_NO_CONTENT)

