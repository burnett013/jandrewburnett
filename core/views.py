from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import JsonResponse
from .models import Project, Experience, BlogPost
import json
import os
import re
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import google.generativeai as genai

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

from django.views.generic import DetailView

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "core/blog_detail.html"
    context_object_name = "post"

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
            # Use Django's built-in EmailMessage class (uses configured SMTP backend in settings.py)
            from django.core.mail import EmailMessage
            
            email_msg = EmailMessage(
                subject=f"Portfolio Contact: Message from {name}",
                body=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['andyburnett013@gmail.com'],
                reply_to=[email]
            )
            email_msg.send()
            
            messages.success(self.request, "Message sent successfully! I'll get back to you soon.")
            logger.info(f"Email sent successfully from {email} via SMTP")
        except Exception as e:
            messages.error(self.request, "An error occurred while sending the message. Please try again later.")
            logger.error(f"Email sending failed: {str(e)}", exc_info=True)

        return super().form_valid(form)


@method_decorator(csrf_exempt, name='dispatch')
class ChatBotView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()
            client_history = data.get('history', [])
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        if not user_message:
            return JsonResponse({'error': 'Message is empty'}, status=400)

        # Get Gemini API key
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            api_key = getattr(settings, "GEMINI_API_KEY", None)

        if not api_key:
            return JsonResponse({
                'response': "Hi! I'm Andy's AI Assistant. I would love to answer your questions, but my Gemini API Key is not yet configured on the server. Please check back later!"
            })

        # Fetch data from DB to dynamically seed the prompt
        try:
            experiences = Experience.objects.all().order_by('-start_date')
            projects = Project.objects.all()
            blog_posts = BlogPost.objects.all().order_by('-published_date')

            # Compile context
            context_str = (
                "You are 'Andy's AI Portfolio Assistant', a professional, friendly, and helpful AI representative for Andy Burnett.\n"
                "Your objective is to answer questions about Andy's resume, work experience, projects, skills, education, and career background based on the database information provided below.\n"
                "If the query is not related to Andy (e.g. asking for unrelated coding tasks, general trivia, weather, cooking recipes), politely direct the conversation back to Andy's portfolio and skills.\n"
                "Keep responses concise (1 to 3 paragraphs max), warm, professional, and formatted in clean Markdown.\n\n"
                "--- BIOGRAPHY AND OVERVIEW ---\n"
                "Name: Andy Burnett (Full: J. Andrew Burnett)\n"
                "Profession: Data Analyst, AI Strategist, and Python Developer.\n"
                "Current Position: Data Analyst in the Research Department at UT Tyler's School of Nursing (started Jan 12, 2026), where he supports research, quality improvement, and evidence-based initiatives for East Texas.\n"
                "Education: M.S. in Artificial Intelligence and Business Analytics from the University of South Florida (USF). B.S. in Entrepreneurship.\n"
                "Military: Former U.S. Army Paratrooper & Platoon Combat Medic (April 2006 — April 2010). Served in Afghanistan, recovered from combat injury, which taught him resilience and calmness under pressure.\n"
                "Family: Married to Elisabeth, father to baby Hollyn.\n\n"
                "--- WORK EXPERIENCE ---\n"
            )

            for exp in experiences:
                end_d = exp.end_date.strftime("%B %Y") if exp.end_date else "Present"
                context_str += f"- Role: {exp.role} at {exp.company}\n  Dates: {exp.start_date.strftime('%B %Y')} — {end_d}\n"
                context_str += "  Bullets:\n"
                for bullet in exp.description_bullets:
                    context_str += f"    * {bullet}\n"
                context_str += "\n"

            context_str += "--- PROJECTS ---\n"
            for proj in projects:
                context_str += f"- Name: {proj.name}\n"
                context_str += f"  Tech Stack: {', '.join(proj.tech_stack)}\n"
                context_str += f"  Description: {proj.description}\n"
                if proj.link:
                    context_str += f"  Link: {proj.link}\n"
                context_str += "\n"

            context_str += "--- BLOG ARTICLES ---\n"
            for post in blog_posts:
                context_str += f"- Title: {post.title}\n"
                clean_content = re.sub('<[^<]+?>', '', post.content)
                context_str += f"  Content Preview: {clean_content[:300]}...\n\n"

            # Setup GenAI SDK
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(
                model_name='gemini-2.5-flash',
                system_instruction=context_str
            )

            # Format history
            formatted_history = []
            for item in client_history:
                role = 'user' if item.get('role') == 'user' else 'model'
                formatted_history.append({
                    'role': role,
                    'parts': [item.get('text', '')]
                })

            chat = model.start_chat(history=formatted_history)
            response = chat.send_message(user_message)
            return JsonResponse({'response': response.text})

        except Exception as e:
            logger.error(f"Error in ChatBotView: {str(e)}", exc_info=True)
            return JsonResponse({'error': f"Failed to get response: {str(e)}"}, status=500)

