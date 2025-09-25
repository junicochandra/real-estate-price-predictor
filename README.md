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
│ ├── main.py # Entry point of the application
│ ├── controllers/ # Request handlers / business logic
│ │ └── arithmetic_controller.py
│ ├── routers/ # API routes (modular)
│ │ └── arithmetic_router.py
│ └── models/ # Pydantic models for validation
│
│── tests/
│ └── test_arithmetic.py # Unit tests with pytest
│
│── requirements.txt # Dependencies
│── Dockerfile # Docker setup
│── docker-compose.yml # Optional docker-compose config
│── README.md # Project documentation
```

## Quick Start

Follow these steps to set up and run the project in your local environment:

### 1. Clone and Rebuild the Docker starter pack

```bash
git clone https://github.com/junicochandra/docker-starterpack.git

cd docker-starterpack

./rebuild
```

### 2. Clone the Python project inside the workspace

```bash
git clone https://github.com/junicochandra/real-estate-price-predictor.git
```

### 3. Access the application in your browser

http://localhost:8080/real-estate/docs

## Running Tests

```bash
cd docker-starterpack

docker-compose exec -it real-estate-price bash

pytest -v
```
