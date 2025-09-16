![Python](https://img.shields.io/badge/python-3.12-blue)
# 🧩 Service Template

This project lets you easily create a new service, with pre-built containerized **development** and **production** setups.

It is designed as a [Copier](https://copier.readthedocs.io/) template, so you can generate a new service project in just a few commands.

---

## 🚀 Getting Started

### 1. Generate a new service

First, install Copier if you don’t have it already:

    pip install copier

Then, create a new service from this template:

    copier copy gh:Durantoine/service-template ./my-new-service

- Replace `./my-new-service` with the path where you want your service to be created.

Copier will ask you a few questions (service name, port, description, …) and scaffold a ready-to-use project.

> ⚠️ **Attention :**
>
> - Make sure **Docker** is installed and running on your machine before starting the service.

---

### 2. Development setup

Move into your new service folder:

    cd my-new-service

Start the development environment:

    make dev-up

This will:

- Build the Docker image for your service in **development mode** (`dev` target).  
- Start the FastAPI app with **hot reload** so your code changes are applied automatically.  
- Mount your local source code into the container for live editing.  

#### Access the FastAPI app

The FastAPI application is exposed on the port you defined when generating the service (for example `8000`).  

Open your browser or use curl:

    http://localhost:8000

You should see your FastAPI app running.

Check logs:

    make dev-logs

Stop the development environment:

    make dev-down

---

### 3. Production setup

To simulate a production deployment locally:

    make prod-up

This will:

- Build the Docker image for your service in **production mode** (`prod` target).  
- Start the FastAPI app with **Uvicorn multi-worker** configuration for production.  

#### Access the FastAPI app in production

Open your browser or curl using the service port:

    http://localhost:8000

Check logs:

    make prod-logs

Stop the production environment:

    make prod-down

---

### 4. Useful commands

| Command            | Description                            |
|--------------------|----------------------------------------|
| `make dev-up`      | Start development containers           |
| `make dev-down`    | Stop development containers            |
| `make dev-logs`    | Show logs from development containers  |
| `make prod-up`     | Start production containers            |
| `make prod-down`   | Stop production containers             |
| `make prod-logs`   | Show logs from production containers   |

---

## 📂 Project structure

A generated service will look like this:

```
my-new-service/
├── compose.yaml                 # Base docker-compose file
├── compose-dev-override.yaml    # Dev-specific overrides
├── compose-prod-override.yaml   # Prod-specific overrides
├── service/                         # Your service source code
├── tests/                       # Your test suite
└── Makefile                     # Useful commands (dev/prod)
```

---

## ✅ Next steps

1. Write your service logic inside `service/`.  
2. Add tests in `tests/`.  
3. Run your service locally with `make dev-up`.  
4. Access the FastAPI app on `http://localhost:8000.  
5. Push it to your own Git repository.  
6. Deploy wherever you want 🚀

---

## 📖 Resources

- [Service Template Repository](https://github.com/Durantoine/service-template)  
- [Copier documentation](https://copier.readthedocs.io/)  
- [Docker Compose documentation](https://docs.docker.com/compose/)  
- [FastAPI documentation](https://fastapi.tiangolo.com/)  

---

Made with ❤️ using Copier & Docker.
