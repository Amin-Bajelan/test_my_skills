from rest_framework import serializers
from blog.models import Post, Category

from django.urls import reverse


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=100)


class PostSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField(read_only=True)
    category_name = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'status', 'category_name',
                  'created_date', 'updated_date', 'published_date', 'absolute_url']

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(
                reverse('post-detail', kwargs={'pk': obj.pk})
            )
        return None

    def get_category_name(self, obj):
        return obj.category.name


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
