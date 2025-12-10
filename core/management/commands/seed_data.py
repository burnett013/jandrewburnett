from django.core.management.base import BaseCommand
from core.models import Experience, Project, BlogPost
from datetime import date

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        # Projects
        p0, created = Project.objects.get_or_create(
            name="AI-Powered Catalog Comparison",
            defaults={
                "tech_stack": ["Python", "Streamlit", "Gemini API"],
                "description": "Built an AI-powered catalog comparison system that uses Gemini 3 Pro to extract and interpret program listings. Reduces manual reconciliation by weeks and improves reporting consistency.",
                "link": "#"
            }
        )

        p1, created = Project.objects.get_or_create(
            name="FAA Full Dataset (300k+ rows)",
            defaults={
                "tech_stack": ["Python", "Pandas", "SQL"],
                "description": "Sourced, cleaned, and structured a national dataset containing every registered aircraft in the U.S., building the foundation for advanced aviation analytics.",
                "link": "https://github.com/jandrewburnett/faa-analysis"
            }
        )
        
        p2, created = Project.objects.get_or_create(
            name="FAA Kits Dataset App",
            defaults={
                "tech_stack": ["FastAPI", "PostgreSQL", "Streamlit"],
                "description": "Created a refined dataset of kit-built aircraft and developed a full-stack application combining database design, data analysis, and visualization.",
            }
        )

        # Experience
        e1, created = Experience.objects.get_or_create(
            role="Special Projects Analyst",
            company="United States Air Force",
            start_date=date(2018, 5, 1),
            end_date=date(2022, 5, 1),
            defaults={
                "description_bullets": [
                    "Led cross-functional teams to optimize logistics workflows.",
                    "Analyzed operational data to improve mission readiness by 15%."
                ]
            }
        )

        e2, created = Experience.objects.get_or_create(
            role="Combat Medic",
            company="United States Air Force",
            start_date=date(2014, 1, 1),
            end_date=date(2018, 5, 1),
            defaults={
                "description_bullets": [
                    "Provided emergency medical care in high-stress environments.",
                    "Managed medical records and supply logistics for a 50-person unit."
                ]
            }
        )

        # Blog
        b1, created = BlogPost.objects.get_or_create(
            slug="hello-world",
            defaults={
                "title": "Hello World: My Journey into Python",
                "content": "This is the start of my personal portfolio. I decided to build this with Django to leverage its powerful Admin interface while keeping the frontend simple with Tailwind CSS. It's a great example of a 'Python-first' web stack."
            }
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))
