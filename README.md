# Real Estate Price Predictor

A **FastAPI-based machine learning project** that provides REST API endpoints to predict real estate prices.  
This project is designed with **clean architecture**, tested with **pytest**, and ready to run in **Docker** for production or local development.

## Features

- **FastAPI** backend with automatic interactive API docs (Swagger & ReDoc).
- **Modular clean architecture** for scalability and maintainability.
- **Arithmetic example endpoints** (add, subtract, multiply, divide) for learning and testing.
- **Unit tests** with `pytest` to ensure reliability.
- **Docker-ready** for seamless deployment.

## Project Structure

```bash
real-estate-price-predictor/
│── app/
│ │
│ ├── adapters/ # Outermost layer: connection to the outside world (API, CLI, etc.)
│ │ ├── handlers/ # Handle incoming requests and delegate them to use cases
│ │ └── routers/ # Routing
│ │
│ ├── core/ # Config & utilities global
│ │
│ ├── domain/ # Application core layer (business rules)
│ │ ├── entities/ # Entity definition (e.g. House, User, etc.)
│ │ └── interfaces/ # Abstraction / contract (e.g. repository interface)
│ │
│ ├── infrastructure/ # Technical implementation (database, external API, etc.)
│ │ └── repositories/ # Implementation repository (MySQL, PostgreSQL, etc.)
│ │
│ ├── services/ # Shared business logic layer, grouping related operations
│ │
│ ├── usecases/ # Application logic / specific business rules
│ │
│ └── main.py # FastAPI entry point
│
│── tests/ # Unit tests
│
│── .gitignore
│── Dockerfile
│── pytest.ini
│── README.md
│── requirements.txt
```

## Quick Start

Follow these steps to set up and run the project in your local environment:

### 1. Clone and Rebuild Docker Starter Pack

```bash
git clone https://github.com/junicochandra/docker-starterpack.git

cd docker-starterpack

./rebuild
```

### 2. Clone Python Project inside the workspace

```bash
git clone https://github.com/junicochandra/real-estate-price-predictor.git
```

### 3. Access application in your browser

http://localhost:8080/real-estate/docs

## Running Tests

To run test suite inside Docker container:

```bash
cd docker-starterpack

docker-compose exec -it real-estate-price bash

pytest -v
```
