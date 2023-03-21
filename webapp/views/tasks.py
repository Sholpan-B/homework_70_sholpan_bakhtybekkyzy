from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import TaskForm
from webapp.models import Task


class ManagerLeadPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['admin', 'Project Manager', 'Team Lead']).exists()


class ManagerLeadDeveloperPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['admin', 'Project Manager', 'Team Lead', 'Developer']).exists()


class TaskDetailView(DetailView):
    template_name = 'tasks/task.html'
    model = Task


class TaskAddView(ManagerLeadDeveloperPermissionMixin, CreateView):
    template_name = 'tasks/task_add.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskUpdateView(ManagerLeadDeveloperPermissionMixin, UpdateView):
    template_name = 'tasks/task_update.html'
    form_class = TaskForm
    model = Task
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(ManagerLeadPermissionMixin, DeleteView):
    template_name = 'tasks/task_confirm_delete.html'
    model = Task
    success_url = reverse_lazy('index')
