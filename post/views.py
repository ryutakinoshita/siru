from audioop import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render,redirect
from post.forms import PostCreateForm
from django.urls import reverse_lazy
from post.models import Post
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
)


class HomeViews(ListView):
    model = Post
    template_name = 'post/home.html'
    context_object_name = 'posts'


class PostCreateView(CreateView,LoginRequiredMixin):#投稿機能
    template_name = 'post/post_create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):#投稿の詳細
    template_name = 'post/post_detail.html'
    model = Post

def comment(request):
    if request.method == "POST":  # 入力フォームはPOSTなので
        form = CommentForm(request.POST)
        if form.is_valid():
            # comment.target = Post
            comment.save()
    else:
        form = CommentForm

    return render(request, 'post/comment.html', {'form': form})



class UpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):#投稿編集機能
    model = Post
    fields = ['title','text']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def get_test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False


class DeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):#投稿削除機能
    model =Post
    success_url = '/'


    def get_test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False


