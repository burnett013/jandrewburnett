# My Personal Website

A professional portfolio website built with Python and Django, styled with Tailwind CSS.

## 🚀 Tech Stack

*   **Backend:** Django 5.x
*   **Database:**
    *   **Local:** SQLite (`db.sqlite3`)
    *   **Production:** PostgreSQL (Railway)
*   **Frontend:** HTML5, Tailwind CSS
*   **Static Files:** WhiteNoise
*   **Hosting:** Railway

## 🛠️ Setup & Local Development

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/burnett013/jandrewburnett.git
    cd jandrewburnett
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Seed the local database:**
    This command populates your local SQLite database with initial Projects, Experience, and Blog Posts.
    ```bash
    python manage.py seed_data
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    Visit `http://127.0.0.1:8000` in your browser.

## 🌍 Production Data & Seeding

**Important:** Your production database (Postgres on Railway) is completely separate from your local database (SQLite). Pushing code to GitHub does *not* push your data.

### How to Update Production Data
Whenever you modify `core/management/commands/seed_data.py` (e.g., adding a new project or job), you must:

1.  **Commit and push** your changes to GitHub:
    ```bash
    git add .
    git commit -m "Update seed data"
    git push
    ```

2.  **Wait for the deployment** to finish on Railway (check the "Deployments" tab).

3.  **Run the seed command on production:**
    You can do this via the [Railway Dashboard](https://railway.app) (Service -> Shell) or using the Railway CLI:
    ```bash
    railway run python manage.py seed_data
    ```

## 📂 Project Structure

*   `config/`: Main Django configuration (`settings.py`, `urls.py`).
*   `core/`: The main application.
    *   `models.py`: Database models (Project, Experience, BlogPost).
    *   `views.py`: Logic for pages (Home, Projects, Resume, Blog).
    *   `templates/core/`: HTML templates.
    *   `static/core/`: CSS, images, and other static assets.
    *   `management/commands/seed_data.py`: The script that defines your portfolio data.
