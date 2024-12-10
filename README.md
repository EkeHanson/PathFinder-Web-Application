---

Job Connect API

**Job Connect API** is a robust backend solution built using Django REST Framework (DRF). It powers a job preparation and connection platform designed to help job seekers and recruiters efficiently connect, share insights, and manage their job-related activities.

---

## Features

### User Management
- User registration, login, and profile management.
- Role-based access for job seekers and recruiters.

### Job Board
- CRUD operations for job postings.
- Job search and filtering by location, industry, and salary.
- Job application tracking.

### Interview Preparation
- Repository of past interview questions, searchable by job or company.
- Share and upvote interview experiences.

### Mentorship
- Mentor profiles with areas of expertise.
- Matchmaking between mentors and mentees.
- Direct messaging for mentorship communication.

### Notifications
- Real-time in-app and email notifications.
- Alerts for interviews, new job postings, and mentorship updates.

---

## Installation and Setup

### Prerequisites
- Python 3.9+
- PostgreSQL 12+
- pip (Python package manager)
- Git

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/job-connect-api.git](https://github.com/EkeHanson/PathFinder-Web-Application.git
   cd job_connect
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.venv` file in the project root:
     ```plaintext
     SECRET_KEY=your-secret-key
     DEBUG=True
     DATABASE_NAME=job_connect
     DATABASE_USER=your-db-user
     DATABASE_PASSWORD=your-db-password
     DATABASE_HOST=localhost
     DATABASE_PORT=5432
     ```
   - Replace `your-secret-key` with a strong secret key.

5. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### Authentication
- `POST /api/users/register/` – Register a new user.
- `POST /api/users/login/` – Login and obtain a JWT token.

### Jobs
- `GET /api/jobs/` – List all jobs.
- `POST /api/jobs/` – Create a new job posting (Recruiter only).
- `GET /api/jobs/{id}/` – Retrieve a specific job.
- `POST /api/jobs/{id}/apply/` – Apply for a job.

### Interviews
- `GET /api/interviews/questions/` – Fetch past interview questions.
- `POST /api/interviews/questions/` – Submit a new question.
- `GET /api/interviews/experiences/` – Fetch interview experiences.

### Mentorship
- `GET /api/mentorship/mentors/` – List mentors.
- `POST /api/mentorship/requests/` – Request mentorship.

### Notifications
- `GET /api/notifications/` – Fetch notifications.

---

## Project Structure

```plaintext
job_connect/
├── manage.py          # Management script
├── job_connect/       # Project settings
│   ├── settings.py    # Settings file
│   ├── urls.py        # Root URL router
├── apps/              # Core apps
│   ├── users/         # User management
│   ├── jobs/          # Job board
│   ├── interviews/    # Interview repository
│   ├── mentorship/    # Mentorship system
│   ├── notifications/ # Notifications
```

---

## Development Notes

### Running Tests
- Run all tests:
  ```bash
  python manage.py test
  ```

### Linting and Code Formatting
- Use `flake8` for linting:
  ```bash
  flake8 .
  ```
- Use `black` for code formatting:
  ```bash
  black .
  ```

### API Documentation
- Install `drf-yasg` for automatic Swagger documentation:
  ```bash
  pip install drf-yasg
  ```
- View API docs at `/swagger/` after running the server.

---

## Deployment

1. Configure `DEBUG=False` in `.venv`.
2. Set up a production-ready database (e.g., PostgreSQL on AWS or Heroku).
3. Use a WSGI server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn job_connect.wsgi:application
   ```

---

## Contributions

We welcome contributions! Please fork this repository, create a feature branch, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
