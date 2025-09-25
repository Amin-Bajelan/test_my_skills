from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView, ListView, DetailView, FormView, UpdateView, DeleteView
from accounts.models import User, Profile
from blog.models import Post
from blog.forms import PostForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# def index(request):
#     return render(request, 'blog/index.html')

class IndexView(TemplateView,LoginRequiredMixin):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.all()
        return context


class ClassRedirectView(RedirectView,LoginRequiredMixin):
    url = 'https://en.wikipedia.org/wiki/Batman'


class ListPostView(ListView,LoginRequiredMixin):
    template_name = 'blog/list_view.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 5

    # def get_queryset(self):
    #     posts = Post.objects.all()
    #     return posts


class PostDetailView(DetailView,LoginRequiredMixin):
    template_name = 'blog/post_detail.html'
    model = Post
    context_object_name = 'post'


class FormPostView(FormView,LoginRequiredMixin):
    template_name = 'blog/post_form.html'
    form_class = PostForm
    success_url = '/blog/list_post/'

    def form_valid(self, form):
        profile = Profile.objects.get(username=self.request.user)
        form.instance.author = profile
        form.instance.status = False
        form.instance.published_date = timezone.now()
        form.save()
        return super().form_valid(form)


class EditPostView(UpdateView,LoginRequiredMixin):
    model = Post
    template_name = 'blog/edit_post.html'
    fields = ['title', 'content', 'status']
    success_url = '/blog/list_post/'

    def form_valid(self, form):
        form.instance.updated_date = timezone.now()
        return super().form_valid(form)


class DeletePostView(DeleteView, LoginRequiredMixin):
    template_name = 'blog/delete_post.html'
    model = Post
    success_url = '/blog/list_post/'
