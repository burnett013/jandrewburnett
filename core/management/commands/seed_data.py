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
                    "<h3 class='text-2xl font-bold text-app-text-main mt-8 mb-4'>Simple Tools for Ensuring Research Data Is Clean, Relevant, and Analysis-Ready</h3>"
                    "<p class='mb-4'>Strong analysis does not begin with statistical software. It begins with how data is planned, collected, organized, and validated.</p>"
                    "<p class='mb-4'>Across industries—healthcare, education, business, and public sector—most analytical challenges trace back to weak data foundations. In my work supporting applied research projects in clinical and academic settings, I have seen that small, early decisions often determine whether a project succeeds or struggles.</p>"
                    "<p class='mb-4'>Fortunately, building analysis-ready data does not require advanced technical tools. It requires disciplined planning and a few reliable practices.</p>"
                    "<p class='mb-6'>Here are practical methods that translate across research and analytics environments.</p>"

                    "<h4 class='text-xl font-bold text-app-text-main mt-8 mb-3'>1. Begin With a Clear Data Plan</h4>"
                    "<p class='mb-3'>Before collecting any data, define:</p>"
                    "<ul class='list-disc pl-6 mb-4 space-y-1'>"
                    "<li>What variables are essential</li>"
                    "<li>How each will be measured</li>"
                    "<li>How participants or records will be tracked</li>"
                    "<li>How datasets will be merged over time</li>"
                    "</ul>"
                    "<p class='mb-4'>In healthcare education projects, this often means clarifying how pre- and post-intervention data will be matched. In business or operations settings, it may involve defining customer or transaction identifiers.</p>"
                    "<p class='mb-6 italic text-app-text-muted'>A short data plan reduces ambiguity and prevents structural problems later.</p>"

                    "<h4 class='text-xl font-bold text-app-text-main mt-8 mb-3'>2. Choose Data Collection Technology Strategically</h4>"
                    "<p class='mb-4'>Data quality is heavily influenced by platform choice.</p>"
                    "<p class='mb-4'>In Microsoft-centered organizations, tools such as Microsoft Forms integrate directly with Excel, Power BI, and automation platforms, enabling efficient downstream workflows. In more complex research environments, platforms like Qualtrics may provide advanced functionality but require greater technical preparation.</p>"
                    "<p class='mb-3'>Best practice across sectors is consistent:</p>"
                    "<ul class='list-disc pl-6 mb-4 space-y-1'>"
                    "<li>Build test surveys</li>"
                    "<li>Export sample data</li>"
                    "<li>Review formats</li>"
                    "<li>Confirm compatibility</li>"
                    "</ul>"
                    "<p class='mb-6 italic text-app-text-muted'>Testing infrastructure early prevents costly redesign.</p>"

                    "<h4 class='text-xl font-bold text-app-text-main mt-8 mb-3'>3. Use Consistent Identifiers</h4>"
                    "<p class='mb-4'>Every record should be traceable through a single, stable identifier.</p>"
                    "<p class='mb-4'>In clinical research, this protects confidentiality while enabling longitudinal analysis. In corporate analytics, it supports accurate customer or asset tracking.</p>"
                    "<p class='mb-3'>Effective identifiers are:</p>"
                    "<ul class='list-disc pl-6 mb-4 space-y-1'>"
                    "<li>Structured</li>"
                    "<li>Non-personal</li>"
                    "<li>Consistently applied</li>"
                    "</ul>"
                    "<p class='mb-6 text-app-text-muted'>This foundation enables reliable integration.</p>"

                    "<h4 class='text-xl font-bold text-app-text-main mt-8 mb-3'>4. Plan for Adequate Sample Size</h4>"
                    "<p class='mb-4'>Data quality includes data quantity.</p>"
                    "<p class='mb-4'>When designing applied research projects, I routinely encourage teams to estimate realistic participation rates. For example, in clinical education studies, anticipated attrition often reduces usable samples by 30–50 percent.</p>"
                    "<p class='mb-4'>If a project begins with ten potential participants, exclusions and non-response may leave too little data for defensible conclusions. The same principle applies in business analytics: insufficient volume weakens inference and forecasting.</p>"
                    "<p class='mb-6 italic text-app-text-muted'>Planning for attrition is essential.</p>"

                    "<h4 class='text-xl font-bold text-app-text-main mt-8 mb-3'>5. Design Instruments With Analysis in Mind</h4>"
                    "<p class='mb-4'>Collection tools should support interpretation. Effective design includes:</p>"
                    "<ul class='list-disc pl-6 mb-4 space-y-1'>"
                    "<li>Consistent response scales</li>"
                    "<li>Clearly defined categories</li>"
                    "<li>Limited free-text fields</li>"
                    "<li>Standardized formats</li>"
                    "</ul>"
                    "<p class='mb-4'>In healthcare surveys, inconsistent scales complicate outcome evaluation. In customer analytics, unstructured inputs reduce usability.</p>"
                    "<p class='mb-6 text-app-text-muted'>Standardization strengthens reliability.</p>"

                    "<h4 class='text-xl font-bold text-app-text-main mt-8 mb-3'>6. Monitor Data Quality During Collection</h4>"
                    "<p class='mb-4'>Waiting until data collection is complete increases risk. Regular reviews should assess:</p>"
                    "<ul class='list-disc pl-6 mb-4 space-y-1'>"
                    "<li>Missing responses</li>"
                    "<li>Outliers</li>"
                    "<li>Duplicates</li>"
                    "<li>Formatting anomalies</li>"
                    "</ul>"
                    "<p class='mb-6 text-app-text-muted'>In applied research environments, early intervention prevents project delays. In operational settings, it reduces rework.</p>"

                    "<h4 class='text-xl font-bold text-app-text-main mt-8 mb-3'>7. Maintain a Data Decision Log</h4>"
                    "<p class='mb-3'>All modifications should be documented. A simple log records:</p>"
                    "<ul class='list-disc pl-6 mb-4 space-y-1'>"
                    "<li>Removed records</li>"
                    "<li>Corrections</li>"
                    "<li>Recoding rules</li>"
                    "<li>Assumptions</li>"
                    "</ul>"
                    "<p class='mb-6 text-app-text-muted'>This practice supports transparency, auditability, and reproducibility across domains.</p>"

                    "<h4 class='text-xl font-bold text-app-text-main mt-8 mb-3'>8. Validate Before Analysis</h4>"
                    "<p class='mb-3'>Before statistical modeling or dashboard development, confirm:</p>"
                    "<ul class='list-disc pl-6 mb-4 space-y-1'>"
                    "<li>Sample size accuracy</li>"
                    "<li>Variable alignment with objectives</li>"
                    "<li>Coding consistency</li>"
                    "<li>Missingness patterns</li>"
                    "</ul>"
                    "<p class='mb-6 text-app-text-muted'>Validation is the final quality gate.</p>"

                    "<h3 class='text-2xl font-bold text-app-text-main mt-12 mb-4'>Building Durable Analytics Foundations</h3>"
                    "<p class='mb-4'>Clean data is not about perfection. It is about intentional design.</p>"
                    "<p class='mb-4'>Across clinical research, education, and enterprise environments, strong analytical outcomes depend on disciplined preparation, documentation, and validation.</p>"
                    "<p class='mb-8'>When organizations invest in these foundational practices, analysts spend less time repairing datasets and more time generating insight. The result is faster decision-making, stronger evidence, and more sustainable analytics systems.</p>"

                    "<hr class='my-8 border-app-border'>"
                    "<a href='/static/core/docs/p1_good_data.pdf' class='inline-flex items-center px-4 py-2 border border-app-accent text-sm font-medium rounded-md text-app-accent hover:bg-app-surface transition-colors' download>"
                    "   <svg class='w-4 h-4 mr-2' fill='none' stroke='currentColor' viewBox='0 0 24 24'><path stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4'></path></svg>"
                    "   Download this guide (PDF)"
                    "</a>"
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
