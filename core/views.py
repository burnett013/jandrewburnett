from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Project, Experience, BlogPost

class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()[:3]
        context['recent_posts'] = BlogPost.objects.order_by('-published_date')[:3]
        return context

class ProjectListView(ListView):
    model = Project
    template_name = "core/project_list.html"
    context_object_name = "projects"

class ResumeView(ListView):
    model = Experience
    template_name = "core/resume.html"
    context_object_name = "experiences"
    ordering = ['-start_date']

class BlogListView(ListView):
    model = BlogPost
    template_name = "core/blog_list.html"
    paginate_by = 5
    ordering = ['-published_date']
