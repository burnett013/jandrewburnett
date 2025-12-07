from django.core.management.base import BaseCommand
from core.models import Experience, Project, BlogPost
from datetime import date

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        # Projects
        p1, created = Project.objects.get_or_create(
            name="FAA Registration Dataset",
            defaults={
                "tech_stack": ["Python", "Pandas", "SQL"],
                "description": "Processed and analyzed the massive FAA aircraft registration database to identify trends in drone ownership.",
                "link": "https://github.com/jandrewburnett/faa-analysis"
            }
        )
        
        p2, created = Project.objects.get_or_create(
            name="Kits Subset Pipeline",
            defaults={
                "tech_stack": ["Docker", "FastAPI", "Streamlit"],
                "description": "End-to-end data pipeline for managing and sub-setting large kit datasets for manufacturing.",
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
