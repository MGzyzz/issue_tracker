from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic import TemplateView, View, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView, \
    RedirectView
from issue_tracker.models.task import Task
from issue_tracker.models.project import Project
from .forms import TaskForms, ProjectForms, SearchForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from accounts.models import User
# Create your views here.


class Home(ListView):
    template_name = 'home.html'
    context_object_name = 'tasks'
    model = Task
    ordering = ['id']
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        context['form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})

        return context

    def get_queryset(self):
        qs = super().get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value)
            qs = qs.filter(query)

        return qs

    def get_allow_empty(self):
        allow_empty = True
        return allow_empty

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search_query')



class Detail(DetailView):
    template_name = 'detail.html'
    model = Task
    context_object_name = 'task'
    pk_url_kwarg = 'id'


class Add(PermissionRequiredMixin, CreateView):
    template_name = 'project/detail.html'
    model = Task
    form_class = TaskForms
    permission_required = 'issue_tracker.add_task'
    permission_denied_message = 'You have no rights'

    def get_success_url(self):
        return reverse_lazy('detail_project', kwargs={'id': self.kwargs['id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['project'] = Project.objects.get(id=self.kwargs['id'])
        context['tasks'] = Task.objects.filter(project=context['project'])
        return context


    def form_valid(self, form):
        form.instance.project_id = self.kwargs['id']
        return super().form_valid(form)



class Edit(UserPassesTestMixin, UpdateView):
    model = Task
    template_name = 'edit.html'
    form_class = TaskForms
    context_object_name = 'task'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('detail', kwargs={'id': self.object.id})

    def test_func(self):
        return self.request.user in self.get_object().project.users.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project
        return context



class Delete(UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'
    success_url = reverse_lazy('home_project')
    pk_url_kwarg = 'id'


    def test_func(self):
        return self.request.user in self.get_object().project.users.all()

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()
        return self.form_valid(self.get_form())

    def form_valid(self, form):
        return redirect(self.success_url)


class HomeProject(ListView):
    template_name = 'project/home.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['id']
    paginate_by = 5

    def get_queryset(self):
        return Project.objects.all().order_by('start_date')


class AddProject(PermissionRequiredMixin, CreateView):
    template_name = 'project/add.html'
    model = Project
    permission_required = 'issue_tracker.add_project'
    permission_denied_message = 'You have no rights'

    form_class = ProjectForms

    def get_success_url(self):
        return reverse('home_project')


class DetailProject(DetailView):
    template_name = 'project/detail.html'
    model = Project
    context_object_name = 'project'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        tasks = Task.objects.filter(project=project)
        context['tasks'] = tasks
        context['form'] = TaskForms
        return context

class EditProject(UserPassesTestMixin, UpdateView):
    model = Project
    template_name = 'project/edit.html'
    form_class = ProjectForms
    context_object_name = 'project'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('detail_project', kwargs={'id': self.object.id})

    def test_func(self):
        return self.request.user in self.get_object().users.all()


class DeleteProject(PermissionRequiredMixin, DeleteView):
    model = Project
    template_name = 'project/home.html'
    context_object_name = 'project'
    success_url = reverse_lazy('home_project')
    pk_url_kwarg = 'id'
    permission_required = 'issue_tracker.delete_project'
    permission_denied_message = 'You have no rights'




class ListUserInProject(PermissionRequiredMixin, ListView):
    template_name = 'project/information_users_In_project.html'
    context_object_name = 'Users'
    model = User
    permission_required = 'accounts.view_user'
    permission_denied_message = 'You have no rights'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs['id']

        project = get_object_or_404(Project, id=project_id)
        context['project'] = project
        return context


class AddUserInProject(DetailView):
    template_name = 'project/information_users_In_project.html'
    model = User

    def post(self, request, *args, **kwargs):
        user_id = request.POST.get('user_id')
        project_id = self.kwargs['id']
        project = get_object_or_404(Project, id=project_id)
        project.users.add(user_id)
        return redirect('list-user-project', project_id)



class DeleteUserProject(UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'project/information_users_In_project.html'
    pk_url_kwarg = 'id'
    permission_required = 'accounts.delete_user'
    permission_denied_message = 'You do not have permission to delete this user.'

    def test_func(self):
        return self.request.user in self.get_object().users.all()

    def get_success_url(self):
        return reverse_lazy('list-user-project', kwargs={'id': self.kwargs['id']})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user_id = request.POST.get('user_id')
        self.object.users.remove(user_id)
        return redirect(self.get_success_url())

