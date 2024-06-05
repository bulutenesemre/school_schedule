# School Schedule Application

This application provides an API for managing school schedules, including classes, subjects, teachers, and schedules.

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/school-schedule.git
cd school-schedule
```

2. Build the Docker images:
```bash
docker-compose build
```

3. Start the Docker containers via up docker compose:
```bash
docker-compose up -d
```

4. Run the migrations:
```bash
docker-compose exec web python manage.py migrate
```

5. Running Tests:
```bash
docker-compose exec web python manage.py test
```

### API Endpoints

- List/Create Classes: GET /class/
- List/Create Subjects: GET /subject/
- List/Create Teachers: GET /teacher/
- List/Create Schedules: GET /schedule/
- Get Class Schedule for Today: GET /schedule/?for_today=true&class_name={class_name}