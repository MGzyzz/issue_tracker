"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from issue_tracker import views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('auth/login', account_views.LoginView.as_view(), name='login'),
    path('auth/logout', account_views.LogoutView.as_view(), name='logout'),
    path('detail/<int:id>', views.Detail.as_view(), name='detail'),
    path('project/<int:id>/add', views.Add.as_view(), name='add'),
    path('edit/<int:id>', views.Edit.as_view(), name='edit'),
    path('<int:id>/delete', views.Delete.as_view(), name='delete'),
    path('project/', views.HomeProject.as_view(), name='home_project'),
    path('project/<int:id>', views.DetailProject.as_view(), name='detail_project'),
    path('project/add/', views.AddProject.as_view(), name='add_project')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
