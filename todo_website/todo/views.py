from django.views import generic
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.
class TodoListView(generic.ListView):
    model = Todo
    template_name = 'todo/home.html'


def create(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-home')

    context = {'form': form}
    return render(request, 'todo/create.html', context)


class TodoDeleteView(generic.DeleteView):
    model = Todo
    success_url = '/'

