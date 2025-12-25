# Event Management System

A robust event management system that handles event creation, ticket management, and attendee tracking. Built with Django and Django REST Framework, this system provides a solid foundation for managing events of any scale.

## Features

- **Event Management**
  - Create and manage events with details like title, description, location, and capacity
  - Set event dates and track active/inactive status
  - Prevent scheduling conflicts with unique event date constraints

- **Ticket System**
  - Generate tickets for events
  - Track ticket usage (used/unused)
  - Monitor remaining capacity in real-time
  - Calculate check-in rates and attendance statistics

- **User Management**
  - Role-based access control (Admin/User)
  - Secure authentication and authorization
  - Admin dashboard for event and ticket management

- **Reporting**
  - Detailed event analytics
  - Ticket usage statistics
  - Capacity tracking and reporting

## Tech Stack

- **Backend**: Django 4.x
- **API**: Django REST Framework
- **Database**: PostgreSQL (configurable)
- **Containerization**: Docker & Docker Compose
- **Authentication**: JWT (JSON Web Tokens)

## Getting Started

### Prerequisites

- Python 3.8+
- Docker and Docker Compose (for containerized deployment)
- PostgreSQL (if running locally without Docker)

### Installation

1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   cd ticket-system
   ```

2. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Update the environment variables as needed

3. Run with Docker (recommended):
   ```bash
   docker-compose up --build
   ```

4. Or run locally:
   ```bash
   python -m venv venv
   source venv/bin/activate  
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Obtain JWT token
- `POST /api/auth/refresh/` - Refresh JWT token

### Events
- `GET /api/events/` - List all events
- `POST /api/events/` - Create a new event (Admin only)
- `GET /api/events/{id}/` - Get event details
- `PUT/PATCH /api/events/{id}/` - Update event (Admin only)
- `DELETE /api/events/{id}/` - Delete event (Admin only)

### Tickets
- `GET /api/events/{event_id}/tickets/` - List tickets for an event
- `POST /api/events/{event_id}/tickets/` - Create new tickets for an event
- `GET /api/tickets/{ticket_id}/` - Get ticket details
- `PATCH /api/tickets/{ticket_id}/check-in/` - Check-in a ticket

## Project Structure

```
src/
├── events/                 # Events app
│   ├── migrations/        # Database migrations
│   ├── tasks/             # Celery tasks
│   ├── views/             # API views
│   ├── admin.py          # Admin interface
│   ├── models.py         # Data models
│   ├── serializers.py    # API serializers
│   ├── signals.py        # Signal handlers
│   └── urls.py          # URL routing
├── tickets/              # Tickets app
├── users/                # User management
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```
