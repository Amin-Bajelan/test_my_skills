from django.urls import path, include
from . import views

urlpatterns = [
    # path('index/', views.index, name='index'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('redirect/', views.ClassRedirectView.as_view(), name='redirect'),
    path('list_post/', views.ListPostView.as_view(), name='list_post'),
    path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post_add/', views.FormPostView.as_view(), name='post_form'),
    path('post_edit/<int:pk>/', views.EditPostView.as_view(), name='post_edit'),
    path('post_delete/<int:pk>/', views.DeletePostView.as_view(), name='post_delete'),
    path('api/v1/',include('blog.api.v1.urls')),
]