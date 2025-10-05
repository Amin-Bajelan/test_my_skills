from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework.exceptions import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100


from django.shortcuts import get_object_or_404


@api_view()
def index(request):
    return Response("Hello, world. You're at the polls index.")


# @api_view(['GET', 'POST'])
# def post_list(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class PostListApi(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class PostListAPI(ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#
#
#
# class PostDetailAPI(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


# class PostDetailAPI(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#
#     def get(self, request, pk):
#         my_post = get_object_or_404(Post, pk=pk)
#         serializer = self.serializer_class(my_post)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         my_post = get_object_or_404(Post, pk=pk)
#         serializer = self.serializer_class(my_post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, pk):
#         my_post = get_object_or_404(Post, pk=pk)
#         my_post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'PUT', 'DELETE'])
# def post_detail(request, pk):
#     my_post = get_object_or_404(Post, pk=pk)
#     if request.method == 'GET':
#         my_data = PostSerializer(my_post)
#         return Response(my_data.data)
#     elif request.method == 'PUT':
#         serializer = PostSerializer(my_post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         my_post.delete()
#         return Response({'message': 'item delete successfully'}, status=status.HTTP_204_NO_CONTENT)


# class PostViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#
#     def list(self, request):
#         serializer = self.serializer_class(self.queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def retrieve(self, request, pk=None):
#         serializer = self.serializer_class(Post.objects.get(pk=pk))
#         return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']
    ordering_fields = ['author', 'id']
    pagination_class = CustomPagination


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    ordering_fields = ['name', 'id']
