from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, RedirectView

from webapp.forms import ProjectForm, UserProjectForm
from webapp.models import Project
from webapp.views.tasks import ManagerLeadPermissionMixin


class ProjectsView(ListView):
    template_name = 'projects/projects.html'
    model = Project
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    template_name = 'projects/project.html'
    model = Project


class GroupPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['admin', 'Project Manager']).exists()


class ProjectAddView(GroupPermissionMixin, LoginRequiredMixin, CreateView):
    template_name = 'projects/add_project.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})

    def from_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(GroupPermissionMixin, LoginRequiredMixin, UpdateView):
    template_name = 'projects/project_update.html'
    form_class = ProjectForm
    model = Project
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(GroupPermissionMixin, LoginRequiredMixin, DeleteView):
    template_name = 'projects/project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('index')


class IndexRedirectView(RedirectView):
    pattern_name = 'projects'


class UserProjectAddView(ManagerLeadPermissionMixin, UpdateView):
    model = Project
    form_class = UserProjectForm
    template_name = 'user_add_to_project.html'

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm('webapp.add_userproject')

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})
