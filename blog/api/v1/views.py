from rest_framework.response import Response
from rest_framework.decorators import api_view
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
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def post_detail(request, pk):
    my_post = get_object_or_404(Post, pk=pk)
    my_data = PostSerializer(my_post)
    return Response(my_data.data)
