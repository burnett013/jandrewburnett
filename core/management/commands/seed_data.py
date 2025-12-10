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
            company="Office of Veteran Success, USF",
            start_date=date(2024, 4, 1),
            defaults={
                "end_date": None, # Present
                "description_bullets": [
                    "Identified, defined, and wrote SOPs for the out-of-state waiver process and tracking.",
                    "Trained team members and instituted tracking protocols to ensure veracity and timeliness.",
                    "Proposed solutions and implemented tools benefitting the department while advancing skills in Python, SQL, SharePoint, and Advanced Excel."
                ]
            }
        )

        e2, created = Experience.objects.get_or_create(
            role="VA Work-study",
            company="USF Office of Veteran Success",
            start_date=date(2023, 3, 1),
            end_date=date(2024, 5, 1),
            defaults={
                "description_bullets": [
                    "Supported military-connected students in navigating federal and state education benefits.",
                    "Authored Standard Operating Procedures to streamline benefit processing.",
                    "Redesigned workflows using MS Forms and Excel, implemented a tracking system that improved accuracy.",
                    "Prevented over $150,000 in tuition waiver losses per semester."
                ]
            }
        )

        e3, created = Experience.objects.get_or_create(
            role="Platoon Combat Medic",
            company="US Army",
            start_date=date(2006, 4, 1),
            end_date=date(2010, 4, 1),
            defaults={
                "description_bullets": [
                    "Provided routine and emergency medical care to a 35-member Paratrooper unit in garrison and combat environments.",
                    "Managed immunizations, pre-deployment screenings, and wellness programs ensuring 100% medical readiness.",
                    "Delivered frontline trauma and mental health support under high-stress conditions."
                ]
            }
        )

        e4, created = Experience.objects.get_or_create(
            role="Roofer",
            company="Resource Roofing",
            start_date=date(2005, 7, 1),
            end_date=date(2006, 4, 1),
            defaults={
                "description_bullets": [
                    "Installed and maintained commercial Thermoplastic Elastomer (TPE) roofing systems.",
                    "Adhered to strict safety standards and company procedures."
                ]
            }
        )

        e5, created = Experience.objects.get_or_create(
            role="Overnight Stocker",
            company="Brookshire Grocery Company",
            start_date=date(2004, 7, 1),
            end_date=date(2005, 7, 1),
            defaults={
                "description_bullets": [
                    "Responsible for receiving, organizing, and restocking frozen goods to maintain optimal shelf availability.",
                    "Ensured inventory accuracy and met restocking deadlines under time-sensitive conditions."
                ]
            }
        )

        e6, created = Experience.objects.get_or_create(
            role="Lumber Truck Driver",
            company="Holly Lake Hardware",
            start_date=date(2004, 1, 1),
            end_date=date(2004, 7, 1),
            defaults={
                "description_bullets": [
                    "Transported up to 12 loads of building materials daily, ensuring timely deliveries.",
                    "Provided direct on-site support and maintained strong face-to-face client relationships."
                ]
            }
        )

        e7, created = Experience.objects.get_or_create(
            role="Courtesy Clerk / Stocker",
            company="Brookshire Grocery Company",
            start_date=date(2002, 1, 1),
            end_date=date(2004, 1, 1),
            defaults={
                "description_bullets": [
                    "Provided extensive customer service and managed front-end store operations."
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
