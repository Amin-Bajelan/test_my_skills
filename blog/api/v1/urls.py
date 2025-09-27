from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('post_list/', views.post_list, name='post_list_api'),
    path('post/detail/<int:pk>/', views.post_detail,name='post_detail_api'),

]