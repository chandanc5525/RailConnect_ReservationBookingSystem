# RailConnect — Railway Booking REST API

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0%2B-D71F00?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

**RailConnect** is a modular, high-performance Railway Reservation RESTful API built using **Python, FastAPI, SQLAlchemy, and SQLite**. It simulates real-world train ticket management—handling train schedules, passenger records, ticket reservations, dynamic seat allocations, and unique PNR generation.

---

##  Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Database Schema](#-database-schema)
- [Project Directory Structure](#-project-directory-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
  - [Running the Application](#running-the-application)
- [API Reference & Usage](#-api-reference--usage)
  - [Endpoints Summary](#endpoints-summary)
  - [Sample Booking Workflow](#sample-booking-workflow)
- [Running Tests](#-running-tests)
- [Future Roadmap](#-future-roadmap)
- [License](#-license)

---

## Overview

The **RailConnect** API is designed to demonstrate clean backend software architecture principles in Python. By separating application routing, request validation, business logic, ORM mappings, and database persistence into decoupled layers, RailConnect provides an easily extensible foundation for complex booking applications.

### Core Business Case
A user wants to book a train journey:
1. Searches available trains for a source and destination.
2. Selects a train and provides passenger information.
3. The system verifies seat availability, deducts inventory atomically, assigns an exact seat number, calculates fare, generates a unique PNR, and returns a confirmed booking receipt.

---

## Key Features

- **Decoupled Layered Architecture**: Strict separation between API Routers, Schemas, Services, and Database Models.
- **Automated PNR Generation**: Dynamic generation of unique 6-digit alphanumeric PNR numbers.
- **Seat Allocation & Inventory**: Real-time checking and updating of seat availability.
- **Strict Data Validation**: Request payload filtering and type-checking via **Pydantic v2**.
- **Interactive Documentation**: Auto-generated Swagger UI and ReDoc endpoints out of the box.
- **Automated Test Suite**: Unit and end-to-end endpoint tests using `pytest` with an isolated in-memory database setup.

---

## Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Language** | [Python 3.10+](https://www.python.org/) | Core programming language |
| **Framework** | [FastAPI](https://fastapi.tiangolo.com/) | Asynchronous web framework for building APIs |
| **ORM** | [SQLAlchemy 2.0](https://www.sqlalchemy.org/) | Object-Relational Mapping & DB session handling |
| **Validation** | [Pydantic v2](https://docs.pydantic.dev/) | Data validation and settings management |
| **Database** | [SQLite](https://www.sqlite.org/) | Lightweight relational database |
| **Server** | [Uvicorn](https://www.uvicorn.org/) | Lightning-fast ASGI server |
| **Testing** | [Pytest](https://docs.pytest.org/) | Framework for automated testing |

---

##  Architecture

RailConnect follows a **5-Layer Architecture** pattern:

```text
                  ┌────────────────────────┐
                  │   HTTP Client / Web    │
                  └───────────┬────────────┘
                              │
                              ▼
    ┌──────────────────────────────────────────────────┐
    │  API / Router Layer (app/routers/)               │
    │  - Receives HTTP Requests & returns Responses    │
    └─────────────────────────┬────────────────────────┘
                              │
                              ▼
    ┌──────────────────────────────────────────────────┐
    │  Schema Layer (app/schemas/)                     │
    │  - Pydantic models for validation & serialization│
    └─────────────────────────┬────────────────────────┘
                              │
                              ▼
    ┌──────────────────────────────────────────────────┐
    │  Service Layer (app/services/)                   │
    │  - Business logic: PNR generation, seat decrement│
    └─────────────────────────┬────────────────────────┘
                              │
                              ▼
    ┌──────────────────────────────────────────────────┐
    │  Data Layer (app/models/ & app/database/)        │
    │  - SQLAlchemy ORM models & database session      │
    └──────────────────────────────────────────────────┘