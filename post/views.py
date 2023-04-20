from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, DetailView, DeleteView

from .forms import CreateForm, CommentForm
from .models import Post, Team
# from .League import LEAGUE_CHOICE

class PostListView(LoginRequiredMixin, ListView):
    template_name = 'post/list.html'
    model = Post
    ordering = ['-created_at']
    paginate_by = 20


class PostCreateView(LoginRequiredMixin, FormView):
    template_name = 'post/create.html'
    form_class = CreateForm
    success_url = reverse_lazy('post:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        create_form = CreateForm(request.POST)
        if create_form.is_valid():
            new_post = create_form.save(commit=False)
            title = create_form.cleaned_data['title']
            team = create_form.cleaned_data['team']
            content = create_form.cleaned_data['content']
            new_post.author = self.request.user
            new_post.save()
            return redirect('post:list')
        return redirect('post:list')


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'post/detail.html'
    model = Post

    def get(self, request, pk):
        post_detail = Post.objects.get(id=pk)
        comment = post_detail.commented_post.all()
        comment_form = CommentForm()
        context = {
            'post': post_detail,
            'comment_form': comment_form,
            'comments': comment
        }
        return render(request, 'post/detail.html', context)

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        post_id = self.kwargs.get('pk')
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            post = Post.objects.get(id=post_id)
            comment.post = post
            comment.author = request.user
            comment.save()
            print('success')
            return redirect('post:detail', pk=post_id)
        return redirect('post:detail', pk=post_id)


class PostDeleteView(DeleteView):
    template_name = 'post/delete.html'
    model = Post
    success_url = reverse_lazy('post:list')