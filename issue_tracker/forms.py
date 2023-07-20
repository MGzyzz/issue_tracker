from django import forms
from .models import Task, Status, Types, Project
from issue_tracker.validator import at_lest, limit_words_description


class TaskForms(forms.ModelForm):
    summary = forms.CharField(required=True, validators=[at_lest], label='summary')
    description = forms.CharField(required=False, validators=[limit_words_description], label='description')
    project = forms.ModelChoiceField(queryset=Project.objects.all(), label='project')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='status', required=True)
    type = forms.ModelChoiceField(queryset=Types.objects.all(), label='type', required=True)

    class Meta:
        model = Task
        fields = ['summary', 'description', 'project', 'status', 'type']
        widgets = {
            'summary': forms.TextInput(attrs={'class': 'partial-control mb-3'}),
            'description': forms.Textarea(attrs={'class': 'partial-control mb-3'}),
            'project': forms.HiddenInput(),
            'status': forms.Select(attrs={'class': 'partial-select mb-3'}),
            'type': forms.Select(attrs={'class': 'partial-select mb-3'}),
        }


class ProjectForms(forms.ModelForm):
    title = forms.CharField(required=True, label='title')
    description = forms.CharField(required=True, label='description')
    start_date = forms.DateField(required=True, label='start_date')
    end_date = forms.DateField(required=False, label='end_date')

    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'partial-control mb-3'})
        }


class SearchForm(forms.Form):
    search_query = forms.CharField(
        max_length=100,
        required=False,
        label='Найти',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'enter search value'
        })
    )