# Real-Time Telemetry Processing API & Data Pipeline

A lightweight, asynchronous FastAPI application designed to process, sanitize, and aggregate streaming sensor/telematics data (e.g., GPS coordinates, speed, vehicle diagnostic metrics) tailored for Intelligent Transportation Systems (ITS).

## 💡 Key Features
- **FastAPI Core:** High-performance RESTful API endpoints utilizing Python `asyncio`.
- **Data Validation:** Strict schema parsing using Pydantic v2 with custom field validators for vehicle IDs and coordinate bounds.
- **Automated Processing:** Real-time sanitization of spatial coordinates, speed limits, and timezone-aware UTC timestamps.
- **Asynchronous Batching:** Optimized stream ingestion endpoint handling batch telemetry payloads with structured reporting.

## 🛠 Tech Stack
- **Language:** Python 3.13
- **Framework:** FastAPI, Uvicorn (ASGI)
- **Validation & Parsing:** Pydantic v2
- **Testing Suite:** Pytest, HTTPX
- **Containerization:** Docker (Slim Debian base)

---

## 🚦 Getting Started

### 1. Prerequisites
Ensure you have Python 3.13+ installed on your local machine.

### 2. Installation & Setup
Clone the repository and set up your local environment:

```bash
# Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate # On windows Powershell

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
