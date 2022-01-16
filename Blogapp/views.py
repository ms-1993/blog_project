from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from Blogapp.models import Post

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from Blogapp.forms import UserCreateForm
from Blogapp.blog_filter import PostFilter


class PostList(generic.ListView):
    # queryset = Post.objects.all()
    model = Post
    template_name = 'blog/index.html'  # a list of all posts will be displayed on index.html

    # def get_queryset(self):
    #     qs = self.model.objects.all()
    #     filtered_model_list = PostFilter(self.request.GET, queryset=qs)
    #     return filtered_model_list.qs

    def get_context_data(self, **kwargs):
        context_data = super(PostList, self).get_context_data(**kwargs)
        f = PostFilter(self.request.GET, queryset=self.get_queryset())
        context_data['filter'] = f
        return context_data


class PostDetail(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # detail about each blog post will be on post_detail.html


# ====================

@method_decorator(login_required, name='dispatch')
class BlogListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


@method_decorator(login_required, name='dispatch')
class BlogCreateView(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('profile')


@method_decorator(login_required, name='dispatch')
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('profile')


@method_decorator(login_required, name='dispatch')
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    success_url = reverse_lazy('profile')
    context_object_name = 'post'


@method_decorator(login_required, name='dispatch')
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('profile')
    context_object_name = 'post'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('home')
    else:
        form = UserCreateForm()
    return render(request, 'registration/signup.html', {'form': form})


def About(request):
    return render(request, 'blog/about.html')
