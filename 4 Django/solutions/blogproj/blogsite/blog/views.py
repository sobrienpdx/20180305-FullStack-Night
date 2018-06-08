from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import BlogPost, Comment

class BlogList(ListView):
    context_object_name = 'blog_list'
    queryset = BlogPost.objects.all().order_by('-timestamp')
    template_name = 'blog/index.html'


class BlogDetail(DetailView):
    model = BlogPost
    template_name = 'blog/detail.html'

    # Extend get_object() to include comments associated with the post
    def get_object(self):
        post = super().get_object()
        comments = Comment.objects.filter(blogpost=post)
        post.comments = comments
        return post


# Equivalent behavior as class based view above
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = Comment.objects.filter(blogpost=post)
    return render(request, 'blog/detail.html', {'blogpost': post, 'comments': comments})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            # add a user to a group
            group = Group.objects.get(name='Commenters')
            user.groups.add(group)
            user.save()

            return redirect('blog:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})