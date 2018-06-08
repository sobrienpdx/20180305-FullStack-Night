from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import Todo

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('todousers:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('todousers:index')


def index(request):
    """ Return the incomplete todos by descending order and completed todos by desscending order.
    """
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user).order_by('completed', '-created_date')
        return render(request, 'todousers/todo_list.html', {'todo_list': todos})

    else:
        return render(request, 'todousers/todo_list.html')

@login_required
def add(request):
    todo_text = request.POST['todo']
    todo_item = Todo(user=request.user, text=todo_text)
    todo_item.save()
    return redirect(reverse('todousers:index'))


@login_required
def toggle_done(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.toggle_completed()
    return redirect('todousers:index')


@login_required
def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo = todo.delete()
    return redirect('todousers:index')
