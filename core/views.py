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

from django.views.generic import FormView
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
import logging
import os

logger = logging.getLogger(__name__)

class ContactView(FormView):
    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        full_message = f"Message from {name} ({email}):\n\n{message}"

        try:
            # Use SendGrid HTTP API instead of SMTP
            from sendgrid import SendGridAPIClient
            from sendgrid.helpers.mail import Mail
            
            sg_message = Mail(
                from_email=settings.DEFAULT_FROM_EMAIL,
                to_emails='andyburnett013@gmail.com',
                subject=f"Portfolio Contact: Message from {name}",
                plain_text_content=full_message
            )
            
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(sg_message)
            
            messages.success(self.request, "Message sent successfully! I'll get back to you soon.")
            logger.info(f"Email sent successfully from {email} via SendGrid API (status: {response.status_code})")
        except Exception as e:
            messages.error(self.request, "An error occurred while sending the message. Please try again later.")
            logger.error(f"Email sending failed: {str(e)}", exc_info=True)

        return super().form_valid(form)
