# Real-Time Telemetry Processing API & Data Pipeline

A lightweight, asynchronous **FastAPI** application designed to process, sanitize, and aggregate streaming sensor/telematics data (e.g., GPS coordinates, speed, vehicle diagnostic metrics).

## 💡 Key Features
- **FastAPI Core:** High-performance RESTful API endpoints utilizing Python `asyncio`.
- **Data Validation:** Strict schema parsing using `Pydantic v2`.
- **Automated Processing:** Dynamic validation of spatial coordinates and timestamp ordering.
- **Export Engine:** Asynchronous batching system for exporting processed metrics into JSON/Parquet storage formats.

## 🛠 Tech Stack
- **Language:** Python 3.13
- **Framework:** FastAPI, Uvicorn
- **Validation & Parsing:** Pydantic
- **Testing:** Pytest, HTTPX

## 🚦 Getting Started

### 1. Installation
```bash
