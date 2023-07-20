from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic import TemplateView, View, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from issue_tracker.models.task import Task
from issue_tracker.models.project import Project
from issue_tracker.models.types_and_statuses import Status, Types
from .forms import TaskForms, ProjectForms, SearchForm
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



    def render_to_response(self, context, **response_kwargs):
        if self.search_value and not context['tasks']:
            raise Http404("Задачи не найдены")

        return super().render_to_response(context, **response_kwargs)

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


class Add(CreateView):
    template_name = 'project/detail.html'
    model = Task
    form_class = TaskForms

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



class Edit(UpdateView):
    model = Task
    template_name = 'edit.html'
    form_class = TaskForms
    context_object_name = 'task'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('detail', kwargs={'id': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Delete(DeleteView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'




class TaskEditView(FormView):
    template_name = 'edit.html'
    form_class = TaskForms

    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(self.form_class.Meta.model, id=kwargs.get('id'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(task=self.task, **kwargs)

    def get_initial(self):
        initial = self.task.__dict__
        print(initial)
        initial['tags'] = self.task.tags.all()


class HomeProject(ListView):
    template_name = 'project/home.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['id']
    paginate_by = 5

    def get_queryset(self):
        return Project.objects.all().order_by('start_date')


class AddProject(CreateView):
    template_name = 'project/add.html'
    model = Project

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