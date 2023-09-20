from django.urls import path
from api.views import TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('detail/<int:pk>', TaskDetailView.as_view(), name='detail-json'),
    path('update/<int:pk>', TaskUpdateView.as_view(), name='update-json'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='delete-json')
]