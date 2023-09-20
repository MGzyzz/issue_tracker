from django.urls import path
from issue_tracker import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('detail/<int:id>', views.TaskDetail.as_view(), name='detail'),
    path('project/<int:id>/add', views.TaskAdd.as_view(), name='add'),
    path('edit/<int:id>', views.TaskEdit.as_view(), name='edit'),
    path('<int:id>/delete', views.TaskDelete.as_view(), name='delete'),
    path('project/', views.HomeProject.as_view(), name='home_project'),
    path('project/<int:id>', views.DetailProject.as_view(), name='detail_project'),
    path('project/add/', views.AddProject.as_view(), name='add_project'),
    path('project/<int:id>/edit', views.EditProject.as_view(), name='edit-project'),
    path('project/<int:id>/delete', views.DeleteProject.as_view(), name='delete-project'),
    path('project/<int:id>/detail', views.ListUserInProject.as_view(), name='list-user-project'),
    path('project/<int:id>/add_user', views.AddUserInProject.as_view(), name='add-user-project'),
    path('project/<int:id>/delete_user', views.DeleteUserProject.as_view(), name='delete-user-project'),
]