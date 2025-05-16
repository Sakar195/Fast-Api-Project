# Task Management API

A FastAPI-based microservice following the 12-Factor App methodology for managing tasks.

## Features

- Create, read, update, and delete tasks
- Async API with FastAPI
- Containerized with Docker
- Environment-based configuration
- Testing with pytest
- CI/CD with GitHub Actions

## 12-Factor App Principles Applied

1. **Codebase**: Single codebase tracked in Git
2. **Dependencies**: Explicitly declared and isolated in requirements.txt
3. **Config**: Stored in environment variables
4. **Backing Services**: (Prepared for, but not implemented in this demo)
5. **Build, Release, Run**: Separated with Docker and GitHub Actions
6. **Processes**: Stateless API with in-memory task store
7. **Port Binding**: Self-contained with its own port binding
8. **Concurrency**: Horizontally scalable API
9. **Disposability**: Fast startup/shutdown with stateless design
10. **Dev/Prod Parity**: Same configuration approach in all environments
11. **Logs**: Treated as event streams (stdout/stderr)
12. **Admin Processes**: (Not applicable for this demo)

## Running Locally

### Prerequisites

- Python 3.8+
- pip
- Docker (optional)

### Setup

1. Clone the repository:

   ```
   git clone https://github.com/Sakar195/Fast-Api-Project.git
   cd fast-api-project
   ```

2. Create a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on the `.env.sample` template.

5. Run the application:

   ```
   uvicorn app.main:app --reload
   ```

6. Access the API at http://localhost:8000
   - API docs: http://localhost:8000/docs

## Running with Docker

1. Build the Docker image:

   ```
   docker build -t task-management-api .
   ```

2. Run the container:
   ```
   docker run -p 8000:8000 -e DEBUG=false task-management-api
   ```

## Testing

Run tests with pytest:

```
pytest app/tests/
```

## API Endpoints

- `GET /health` - Health check endpoint
- `GET /api/v1/tasks/` - List all tasks
- `POST /api/v1/tasks/` - Create a new task
- `GET /api/v1/tasks/{task_id}` - Get a specific task
- `PATCH /api/v1/tasks/{task_id}` - Update a task
- `DELETE /api/v1/tasks/{task_id}` - Delete a task

## License

MIT
