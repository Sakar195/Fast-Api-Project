# Getting Started

This guide will help you set up and run the Task Management API on your local machine.

## Prerequisites

- Python 3.8+
- Docker and Docker Compose (optional)
- Git

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/task-management-api.git
cd task-management-api
```

### Using Python (Local Development)

1. Create a virtual environment:

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

Create a `.env` file in the root directory with the following content:

```
PROJECT_NAME="Task Management API"
DEBUG=true
BACKEND_CORS_ORIGINS=["http://localhost:3000","http://localhost:8000"]
```

4. Run the application:

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000.

### Using Docker

1. Build and start the containers:

```bash
docker-compose up -d
```

The API will be available at http://localhost:8000.

## Testing

Run the tests with pytest:

```bash
pytest app/tests/
```

## Development Workflow

1. Create a new branch for your feature:

```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit them:

```bash
git add .
git commit -m "Add your feature"
```

3. Push your changes and create a pull request:

```bash
git push origin feature/your-feature-name
```

4. Run pre-commit hooks to ensure code quality:

```bash
pre-commit install  # Only needed once
pre-commit run --all-files
```

## API Documentation

Once the application is running, you can access the interactive API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
