from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('blog/', views.BlogListView.as_view(), name='blog_list'), # List page
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'), # Detail page
    path('contact/', views.ContactView.as_view(), name='contact'),
]