from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Todo

class IndexView(generic.ListView):
	template_name = 'todosapp/todo_list.html'
	context_object_name = 'todo_list'

	def get_queryset(self):
		""" Return the incomplete todos by descending order and completed todos by desscending order.
		"""
		return Todo.objects.order_by('completed', '-created_date')


class DetailView(generic.DetailView):
	model = Todo
	template_name = 'todosapp/detail.html'


def add(request):
    todo_text = request.POST['todo']
    todo_item = Todo(text=todo_text)
    todo_item.save()
    return HttpResponseRedirect(reverse('todosapp:index'))


def edit(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	if request.method == 'POST':
		form = TodoForm(request.POST, instance=todo)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.author = request.user
			todo.publish()
			return redirect('blog:detail', pk=pk)
	else:
		form = TodoForm(instance=todo)
	return render(request, 'todos/edit_todo.html', {'form': form, 'pk':pk})		


def toggle_done(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	todo.toggle_completed()
	return redirect('todosapp:index')


def delete(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	todo = todo.delete()
	return redirect('todosapp:index')
