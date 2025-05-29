# Hospital Management System

A comprehensive REST API backend for managing hospital operations, doctor profiles, patient appointments, and healthcare services. Built with Django REST Framework for scalability and reliability.

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Database Models](#database-models)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

### Core Features
- **Multi-role Authentication**: Support for Doctor and Patient user roles with JWT token-based authentication
- **Doctor Management**: Comprehensive doctor profiles with specializations, certifications, languages, and awards
- **Appointment Scheduling**: Full appointment booking and management system with time slot management
- **Hospital Management**: Multiple hospital locations and management
- **Email Verification**: Secure email verification during registration
- **CORS Support**: Cross-Origin Resource Sharing enabled for frontend integration

### Security Features
- JWT (JSON Web Tokens) authentication
- Custom user model with role-based access control
- Email verification workflow
- Password reset functionality with secure tokens
- Permission-based access control

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | Django 5.1.7 |
| **REST API** | Django REST Framework |
| **Authentication** | JWT (Simple JWT) |
| **Database** | Django ORM (configurable) |
| **CORS** | django-cors-headers |
| **Task Scheduling** | Django Management Commands |
| **Environment Management** | python-dotenv |

---

## 📁 Project Structure

```
Hospital-Management-System/
├── authentication/          # User authentication & authorization
│   ├── models.py           # Custom User model
│   ├── serializers.py      # Request/response serializers
│   ├── views.py            # Authentication endpoints
│   ├── urls.py             # Authentication routes
│   ├── permissions.py      # Custom permission classes
│   └── backends.py         # Custom authentication backends
│
├── doctors/                 # Doctor management
│   ├── models.py           # Doctor, Specialization, Certification, etc.
│   ├── serializers.py      # Doctor data serialization
│   ├── views.py            # Doctor endpoints
│   └── urls.py             # Doctor routes
│
├── patients/               # Patient management
│   ├── models.py           # Patient profile model
│   ├── serializers.py      # Patient serializers
│   ├── views.py            # Patient endpoints
│   └── urls.py             # Patient routes
│
├── appointments/           # Legacy appointments (deprecated)
│   └── ...
│
├── new_appointments/       # Appointment scheduling system
│   ├── models.py           # PatientAppointment, TimeSlot models
│   ├── serializers.py      # Appointment serializers
│   ├── views.py            # Appointment endpoints
│   ├── urls.py             # Appointment routes
│   └── management/
│       └── commands/
│           └── generate_timeslots.py  # Auto-generate time slots
│
├── healthycare/            # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Root URL configuration
│   ├── wsgi.py             # WSGI application
│   └── asgi.py             # ASGI application
│
├── requirements.txt        # Python dependencies
├── manage.py               # Django management script
└── README.md               # This file
```

---

## 📦 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)
- Git

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Hospital-Management-System.git
cd Hospital-Management-System
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### Environment Setup

Create a `.env` file in the project root directory:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration (if using custom database)
# DATABASE_URL=your-database-url

# Email Configuration (for verification)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# JWT Settings
JWT_SECRET_KEY=your-jwt-secret-key
JWT_EXPIRATION_HOURS=24
```

### Database Configuration

Update `healthycare/settings.py` for your database choice (SQLite, PostgreSQL, MySQL, etc.):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

---

## ▶️ Running the Application

### 1. Apply Migrations

```bash
python manage.py migrate
```

### 2. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 3. Generate Time Slots (Optional)

```bash
python manage.py generate_timeslots
```

### 4. Start the Development Server

```bash
python manage.py runserver
```

The API will be available at: `http://localhost:8000/`

Access the Django admin panel at: `http://localhost:8000/admin/`

---

## 📡 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-----------|
| POST | `/api/auth/register/` | Register new user |
| POST | `/api/auth/login/` | User login (returns JWT token) |
| POST | `/api/auth/refresh/` | Refresh JWT token |
| POST | `/api/auth/verify-email/` | Verify email with code |
| POST | `/api/auth/reset-password/` | Request password reset |

### Doctors
| Method | Endpoint | Description |
|--------|----------|-----------|
| GET | `/api/doctors/` | List all doctors |
| GET | `/api/doctors/{id}/` | Get doctor details |
| POST | `/api/doctors/` | Create doctor profile (admin) |
| PUT | `/api/doctors/{id}/` | Update doctor profile |
| DELETE | `/api/doctors/{id}/` | Delete doctor (admin) |

### Appointments
| Method | Endpoint | Description |
|--------|----------|-----------|
| GET | `/api/appointments/` | List all appointments |
| POST | `/api/appointments/` | Book new appointment |
| GET | `/api/appointments/{id}/` | Get appointment details |
| PUT | `/api/appointments/{id}/` | Update appointment |
| DELETE | `/api/appointments/{id}/` | Cancel appointment |

### Patients
| Method | Endpoint | Description |
|--------|----------|-----------|
| GET | `/api/patients/` | List all patients |
| GET | `/api/patients/{id}/` | Get patient details |
| POST | `/api/patients/` | Create patient profile |
| PUT | `/api/patients/{id}/` | Update patient profile |

---

## 🔐 Authentication

This API uses **JWT (JSON Web Tokens)** for authentication.

### Login Flow

1. **Register**: POST request to `/api/auth/register/` with email, username, password
2. **Verify Email**: Check email for verification code and POST to `/api/auth/verify-email/`
3. **Login**: POST to `/api/auth/login/` to receive JWT tokens
4. **Access**: Include token in request headers: `Authorization: Bearer <your_token>`

### Example Request with JWT

```bash
curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..." http://localhost:8000/api/doctors/
```

---

## 🗄️ Database Models

### User Model (Custom)
- email (unique)
- username
- role (Doctor/Patient)
- is_verified
- verification_code
- password (hashed)

### Doctor Model
- user (OneToOne relationship with User)
- specialization
- certifications
- languages
- awards
- experience
- ratings

### Patient Model
- user (OneToOne relationship with User)
- phone
- date_of_birth
- medical_history

### Appointment Model
- patient (ForeignKey)
- doctor (ForeignKey)
- appointment_date
- timeslot (ForeignKey)
- status (scheduled, in-progress, completed, cancelled)
- reason_to_visit
- department_name

### TimeSlot Model
- doctor (ForeignKey)
- start_time
- end_time
- available

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Write unit tests for new features
- Keep commits atomic and descriptive
- Update documentation accordingly

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 💡 Support

For issues, questions, or suggestions, please open an issue on GitHub or contact the development team.

---

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG=False` in settings
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Use a production-grade database (PostgreSQL recommended)
- [ ] Set up proper email configuration
- [ ] Use environment variables for sensitive data
- [ ] Enable HTTPS
- [ ] Configure CORS for your frontend domain
- [ ] Set up logging and monitoring
- [ ] Run security checks: `python manage.py check --deploy`

### Deployment Options
- Heroku
- AWS (EC2, Elastic Beanstalk)
- DigitalOcean
- PythonAnywhere
- Docker containers

---

**Happy coding! 🎉**