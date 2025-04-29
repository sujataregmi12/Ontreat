# Project Management System

A project management system is a web based application that plans, organizes, tracks and manages projects, developers, teams, and
tasks to ensure that work is completed properly within the designated timelines.

# Features

-User authentication and role management
-Admin interface for managing developers, teams, projects, and tasks
-Project creation and tracking
-Task assignment and tracking
-Project and task deadlines
-Developer profiles
-Team management
-Access control(Admin can view all data, No team member can see developers from other teams)

# Tech stack

-Python 3.12.4
-django 5.1.6
-Bootstrap 5.3.x (frontend)
-SQLite for development
-JavaScript (custom scripts)

# Project Structure

-'projects/' – Handles project creation, assignment, and tracking
-'developers/' – Manages developer profiles and visibility settings
-'teams/' -Team creation, developer assignments, and team lead management
-'tasks/' -Task creation and management, including priority, status, and deadline features
-'core/' – Core settings, URLs, and shared utilities
-'static/' – Static files like CSS and images
-'templates/' – Reusable HTML templates for frontend pages
-'manage.py' – Django’s command-line utility for administrative tasks


1. **Clone the repository**

   '''sh
   git clone <repo-url>
   cd Ontreat
   '''
   
 3. **Create and activate a virtual environment**
     '''sh
     python -m venv env
     source env/bin/activate
     '''
 
 4. **Install dependencies**
     '''sh
     pip install -r requirements.txt
     '''
 
 5. **Apply migrations**
     '''sh
     python manage.py migrate
     '''
 
 6. **Create a superuser (admin)**
     '''sh
     python manage.py createsuperuser
     '''
 
 7. **Run the development server**
     '''sh
     python manage.py runserver
     '''
 
 8. **Access the app**
     - Visit [http://localhost:8000/](http://localhost:8000/) in your browser.


# Testing
 
 To run tests:
 '''sh
 python manage.py test
 '''
 
# File Uploads
 
 - Supported formats: PDF, JPG, PNG, DOC, DOCX.
 - Files are stored in the 'media/' directory

# Environment Variables
 
 - Copy '.env.example' to '.env' and set your environment variables as needed.
 
 # License
 
 This project is for educational/demo purposes. See 'LICENSE' for details.
 

















