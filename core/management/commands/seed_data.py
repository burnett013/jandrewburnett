from django.core.management.base import BaseCommand
from core.models import Experience, Project, BlogPost
from datetime import date


class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        # ---------- Projects Page ----------
        # Repo name: ovs_reporting_v2
        Project.objects.update_or_create(
            name="AI-Powered Catalog Comparison",
            defaults={
                "tech_stack": ["Python", "Streamlit", "Gemini API"],
                "description": (
                    "Built an AI-powered catalog comparison system that uses "
                    "Gemini models to extract and interpret program listings. "
                    "Reduces manual reconciliation by weeks and improves "
                    "reporting consistency."
                ),
                "link": "https://github.com/burnett013/ovs_reporting_v2",
            },
        )

        # Repo name: faa_data
        Project.objects.update_or_create(
            name="FAA Full Dataset (300k+ rows)",
            defaults={
                "tech_stack": ["Python", "Pandas", "SQL"],
                "description": (
                    "Sourced, cleaned, and structured a national dataset "
                    "containing every registered aircraft in the U.S., "
                    "building the foundation for advanced aviation analytics."
                ),
                "link": "https://github.com/burnett013/faa_data",
            },
        )

        # Repo name: nssrn
        Project.objects.update_or_create(
            name="Nursing Workforce Data Dashboard",
            defaults={
                "tech_stack": ["FastAPI", "SQLite", "Streamlit"],
                "description": (
                    "A full-stack analytics dashboard that processes the 2022 "
                    "National Sample Survey of Registered Nurses to visualize "
                    "key workforce trends in burnout, earnings, and telehealth "
                    "adoption."
                ),
                "link": "https://github.com/burnett013/nssrn",
            },
        )

        # Repo name: faa_kit_aircraft_main
        Project.objects.update_or_create(
            name="FAA Kit-built Aircraft Subset",
            defaults={
                "tech_stack": [
                    "Docker",
                    "FastAPI",
                    "Jupyter Notebook",
                    "Python",
                    "Streamlit",
                    "Excel",
                ],
                "description": (
                    "End-to-end data pipeline for managing and sub-setting "
                    "large datasets, focusing on kit-built aircraft registered "
                    "in the US"
                ),
                "link": "https://github.com/burnett013/faa_kit_aircraft_main",
            },
        )

        
        # ---------- Experience Page ----------
        Experience.objects.update_or_create(
            role="Data Analyst",
            company="UT Tyler School of Nursing",
            start_date=date(2026, 1, 12),
            defaults={
                "end_date": None,  # Present
                "description_bullets": [
                    "Leading data analysis initiatives for the School of Nursing.",
                    "Developing insights to support strategic decision-making.",
                ],
            },
        )

        Experience.objects.update_or_create(
            role="Special Projects Analyst",
            company="Office of Veteran Success, USF",
            start_date=date(2024, 4, 1),
            defaults={
                "end_date": None,  # Present
                "description_bullets": [
                    "Identified, defined, and wrote SOPs for the out-of-state waiver process and tracking.",
                    "Trained team members and instituted tracking protocols to ensure veracity and timeliness.",
                    "Proposed solutions and implemented tools benefitting the department while advancing skills in Python, SQL, SharePoint, and Advanced Excel.",
                ],
            },
        )

        Experience.objects.update_or_create(
            role="VA Work-study",
            company="USF Office of Veteran Success",
            start_date=date(2023, 3, 1),
            defaults={
                "end_date": date(2024, 5, 1),
                "description_bullets": [
                    "Supported military-connected students in navigating federal and state education benefits.",
                    "Authored Standard Operating Procedures to streamline benefit processing.",
                    "Redesigned workflows using MS Forms and Excel, implemented a tracking system that improved accuracy.",
                    "Prevented over $150,000 in tuition waiver losses per semester.",
                ],
            },
        )

        Experience.objects.update_or_create(
            role="Platoon Combat Medic",
            company="US Army",
            start_date=date(2006, 4, 1),
            defaults={
                "end_date": date(2010, 4, 1),
                "description_bullets": [
                    "Provided routine and emergency medical care to a 35-member Paratrooper unit in garrison and combat environments.",
                    "Managed immunizations, pre-deployment screenings, and wellness programs ensuring 100% medical readiness.",
                    "Delivered frontline trauma and mental health support under high-stress conditions.",
                ],
            },
        )

        Experience.objects.update_or_create(
            role="Roofer",
            company="Resource Roofing",
            start_date=date(2005, 7, 1),
            defaults={
                "end_date": date(2006, 4, 1),
                "description_bullets": [
                    "Installed and maintained commercial Thermoplastic Elastomer (TPE) roofing systems.",
                    "Adhered to strict safety standards and company procedures.",
                ],
            },
        )

        Experience.objects.update_or_create(
            role="Overnight Stocker",
            company="Brookshire Grocery Company",
            start_date=date(2004, 7, 1),
            defaults={
                "end_date": date(2005, 7, 1),
                "description_bullets": [
                    "Responsible for receiving, organizing, and restocking frozen goods to maintain optimal shelf availability.",
                    "Ensured inventory accuracy and met restocking deadlines under time-sensitive conditions.",
                ],
            },
        )

        Experience.objects.update_or_create(
            role="Lumber Truck Driver",
            company="Holly Lake Hardware",
            start_date=date(2004, 1, 1),
            defaults={
                "end_date": date(2004, 7, 1),
                "description_bullets": [
                    "Transported up to 12 loads of building materials daily, ensuring timely deliveries.",
                    "Provided direct on-site support and maintained strong face-to-face client relationships.",
                ],
            },
        )

        Experience.objects.update_or_create(
            role="Courtesy Clerk / Stocker",
            company="Brookshire Grocery Company",
            start_date=date(2002, 1, 1),
            defaults={
                "end_date": date(2004, 1, 1),
                "description_bullets": [
                    "Provided extensive customer service and managed front-end store operations.",
                ],
            },
        )

        # ---------- Blog Page ----------
        BlogPost.objects.update_or_create(
            slug="good-data-practice",
            defaults={
                "title": "Clean Data: The Foundation of Valid Analysis",
                "content": (
                    "Why \"Good\" Data Matters More Than Complex Algorithms. "
                    "In the rush to apply machine learning and advanced statistics, the foundational step of data cleaning is often overlooked. "
                    "However, as the old adage goes: Garbage In, Garbage Out. "
                    "<br><br>"
                    "Having worked with large datasets ranging from FAA aircraft registries to nursing workforce surveys, I've learned that 80% of the work is just getting the data ready. "
                    "Without rigorous cleaning—handling missing values, standardizing formats, and verifying outliers—even the most sophisticated model will yield misleading results."
                    "<br><br>"
                    "I've compiled a short guide on some best practices for data cleaning, specifically for DNP projects."
                    "<br><br>"
                    "<a href='/static/core/docs/p1_good_data.docx' class='text-app-accent hover:underline font-bold' download>Download the full guide (DOCX)</a>"
                ),
            },
        )

        
        BlogPost.objects.update_or_create(
            slug="hello-world",
            defaults={
                "title": "Hello World: My Journey into Python",
                "content": (
                    "This is the start of my personal portfolio. I decided to build this "
                    "with Django to leverage its powerful Admin interface while keeping "
                    "the frontend simple with Tailwind CSS. It's a great example of a "
                    "'Python-first' web stack."
                ),
            },
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))
