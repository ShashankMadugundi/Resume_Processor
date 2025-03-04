# Resume Processor

This project is a Django-based application that processes resumes to extract key information such as the candidate's first name, email address, and mobile number. The extracted data is stored in a PostgreSQL database, and the application provides a REST API for interaction.

---

## **Features**
- Accepts resume files in PDF or DOCX format via a REST API endpoint.
- Extracts the candidate's first name, email address, and mobile number.
- Saves extracted data to a PostgreSQL database.
- Built with Django and Django REST Framework.

---

## **Getting Started**

### **Prerequisites**
Ensure you have the following installed on your machine:
- Python (>= 3.8)
- PostgreSQL
- pip (Python package manager)
- Virtualenv (optional but recommended)

### **Setup Instructions**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ShashankMadugundi/Resume_Processor
   cd resume-processor


2. Set Up a Virtual Environment

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate


3. Install Dependencies Install the required Python packages from requirements.txt:

bash
Copy code
pip install -r requirements.txt


4. Configure PostgreSQL

Create a new PostgreSQL database named resume_processor.
Update the DATABASES configuration in settings.py:
python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'resume_processor',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


5. Apply Migrations

bash
Copy code
python manage.py makemigrations
python manage.py migrate


6. Run the Development Server

bash
Copy code
python manage.py runserver

The server will be available at http://127.0.0.1:8000.
