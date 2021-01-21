from audioop import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render,redirect, get_object_or_404
from post.forms import PostCreateForm,CommentForm
from django.urls import reverse_lazy
from post.models import Post,Comment
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
)


class HomeViews(ListView):#ホーム表示
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


class CommentView(CreateView,LoginRequiredMixin):
    template_name = 'post/comment.html'
    model = Comment
    form_class = CommentForm


    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect('detail',pk=post_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context




