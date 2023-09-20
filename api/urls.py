from django.urls import path
from api.views import TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('detail/<int:id>', TaskDetailView.as_view(), name='detail-json'),
    path('update/<int:id>', TaskUpdateView.as_view(), name='update-json'),
    path('delete/<int:id>', TaskDeleteView.as_view(), name='delete-json')
]