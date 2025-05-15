# API Reference

The Task Management API provides endpoints for managing tasks.

## Base URL

All endpoints are relative to the base URL of the API: `/api/v1`

## Authentication

Currently, no authentication is required (for demonstration purposes).

## Endpoints

### Health Check

```
GET /health
```

Returns the health status of the API.

**Example Response:**

```json
{
  "status": "healthy",
  "service": "Task Management API"
}
```

### List Tasks

```
GET /api/v1/tasks/
```

Returns a list of all tasks.

**Example Response:**

```json
[
  {
    "id": 1,
    "title": "Complete project",
    "description": "Finish the 12-factor app project",
    "status": "todo",
    "created_at": "2023-05-15T10:00:00",
    "updated_at": "2023-05-15T10:00:00"
  },
  {
    "id": 2,
    "title": "Write tests",
    "description": "Create comprehensive test suite",
    "status": "in_progress",
    "created_at": "2023-05-15T11:00:00",
    "updated_at": "2023-05-15T11:30:00"
  }
]
```

### Create Task

```
POST /api/v1/tasks/
```

Creates a new task.

**Request Body:**

```json
{
  "title": "New task",
  "description": "Description of the new task",
  "status": "todo"
}
```

**Example Response:**

```json
{
  "id": 3,
  "title": "New task",
  "description": "Description of the new task",
  "status": "todo",
  "created_at": "2023-05-15T14:30:00",
  "updated_at": "2023-05-15T14:30:00"
}
```

### Get Task

```
GET /api/v1/tasks/{task_id}
```

Returns a specific task by ID.

**Example Response:**

```json
{
  "id": 1,
  "title": "Complete project",
  "description": "Finish the 12-factor app project",
  "status": "todo",
  "created_at": "2023-05-15T10:00:00",
  "updated_at": "2023-05-15T10:00:00"
}
```

### Update Task

```
PATCH /api/v1/tasks/{task_id}
```

Updates a specific task by ID.

**Request Body:**

```json
{
  "status": "done"
}
```

**Example Response:**

```json
{
  "id": 1,
  "title": "Complete project",
  "description": "Finish the 12-factor app project",
  "status": "done",
  "created_at": "2023-05-15T10:00:00",
  "updated_at": "2023-05-15T15:45:00"
}
```

### Delete Task

```
DELETE /api/v1/tasks/{task_id}
```

Deletes a specific task by ID.

**Response:** HTTP 204 No Content
