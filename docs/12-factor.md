# 12-Factor Principles

This project implements the [12-Factor App methodology](https://12factor.net/), a set of best practices for building software-as-a-service applications that:

- Use declarative formats for setup automation
- Have a clean contract with the operating system
- Are suitable for deployment on modern cloud platforms
- Minimize divergence between development and production
- Can scale up without significant changes to tooling, architecture, or development practices

## Implementation Details

### I. Codebase

- Single codebase tracked in Git
- Clear repository structure with conventional layout

### II. Dependencies

- Explicit dependencies declared in `requirements.txt`
- Virtual environment isolation
- Pinned versions for reproducible builds

### III. Config

- Environment variables via `.env` file
- Pydantic settings management with validation
- No hardcoded configuration values in code

### IV. Backing Services

- Redis included as an example backing service
- Services treated as attached resources
- Easy to swap implementations without code changes

### V. Build, Release, Run

- Docker build process separates build and run stages
- GitHub Actions workflow enforces stages
- Clear separation of code from deployed instances

### VI. Processes

- Stateless processes with no shared memory or filesystem
- In-memory tasks store (could be replaced with a database)
- No session state stored in the application

### VII. Port Binding

- Self-contained web server with port binding
- Export services via port binding
- Containerized for unified interface

### VIII. Concurrency

- Horizontally scalable through process model
- Asynchronous API with FastAPI
- Independent, isolated process design

### IX. Disposability

- Fast startup and graceful shutdown
- Resilient to crashes
- Designed for quick deployment and scaling

### X. Dev/Prod Parity

- Same environment variables structure in all environments
- Docker provides consistent runtime environment
- Minimal differences between environments

### XI. Logs

- Treated as event streams
- Written to stdout/stderr
- No log file management in application code

### XII. Admin Processes

- One-off management tasks as part of the codebase
- Admin tools governed by the same deployment and process isolation
- Run in identical environment as regular processes
