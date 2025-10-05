from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='post')
router.register('category', views.CategoryViewSet, basename='category')
urlpatterns = router.urls

# urlpatterns = [
    # path('index/',views.index,name='index'),
    # path('post_list/', views.PostListAPI.as_view(), name='post_list_api'),
    # path('post_detail/<int:pk>/', views.PostDetailAPI.as_view(), name='post_detail_api'),
    # path('post/', views.PostViewSet.as_view({"get": "list","post": "create"}), name='post'),
    # path('post/<int:pk>/', views.PostViewSet.as_view({"get": "retrieve"}), name='post'),
# ]
