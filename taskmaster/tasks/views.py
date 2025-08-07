from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import TaskForm, UserRegisterForm
from django.contrib.auth.views import LoginView
from django.db.models import Q

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! Please log in.')
            return redirect('tasks:login')
    else:
        form = UserRegisterForm()
    return render(request, 'tasks/register.html', {'form': form})


# Task list view with filtering
@login_required(login_url='tasks:login')
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    
    # Filter by completion status
    status = request.GET.get('status')
    priority = request.GET.get('priority')
    if status == 'completed':
        tasks = tasks.filter(completed=True)
    elif status == 'pending':
        tasks = tasks.filter(completed=False)
    
    # Filter by priority
    if priority in ['low', 'medium', 'high']:
        tasks = tasks.filter(priority=priority)
    
    context = {'tasks': tasks, 'status': status, 'priority': priority}
    return render(request, 'tasks/task_list.html', context)


# Task detail view
@login_required(login_url='tasks:login')
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})


# Create new task
@login_required(login_url='tasks:login')
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully.')
            return redirect('tasks:task-list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


# Update existing task
@login_required(login_url='tasks:login')
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully.')
            return redirect('tasks:task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


# Delete task
@login_required(login_url='tasks:login')
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully.')
        return redirect('tasks:task-list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


# Custom login view with error message
class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)
