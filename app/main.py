from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, field_validator
from datetime import datetime, timezone
from typing import List, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("telemetry-pipeline")

app = FastAPI(
    title="TransTech Telemetry Pipeline API",
    description="Real-time vehicle and sensor telemetry data ingestion service.",
    version="1.0.0",
)

# --- DATA SCHEMAS ---
class TelemetryPayload(BaseModel):
    vehicle_id: str = Field(..., example="VH-10492")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    latitude: float = Field(..., ge=-90.0, le=90.0)
    longitude: float = Field(..., ge=-180.0, le=180.0)
    speed_mph: float = Field(..., ge=0.0, le=200.0)
    engine_temp_c: Optional[float] = Field(None, ge=-40.0, le=150.0)

    @field_validator("vehicle_id")

    def validate_vehicle_id(cls, v: str) -> str:
        if not v.isalnum() and "-" not in v:
            raise ValueError("Vehicle ID must be alphanumeric and may contain hyphens.")
        return v

class BatchIngestResponse(BaseModel):
    status: str
    records_processed: int
    failed_records: int

# --- ENDPOINTS ---
@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now(timezone.utc).isoformat()}

@app.post("/api/v1/telemetry", response_model=BatchIngestResponse, status_code=status.HTTP_201_CREATED)
async def ingest_telemetry_stream(payloads: List[TelemetryPayload]):
    """
    Ingest a batch of streaming telemetry logs from connected vehicles/sensors.
    """
    if not payloads:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Payload batch cannot be empty."
        )

    processed_count = 0
    failed_count = 0

    for item in payloads:
        try:
            # Simulated telemetry processing & pipeline dispatch
            logger.info(f"Ingested telemetry for {item.vehicle_id} at ({item.latitude}, {item.longitude})")
            processed_count += 1
        except Exception as e:
            logger.error(f"Error processing item for vehicle {item.vehicle_id}: {str(e)}")
            failed_count += 1

    return BatchIngestResponse(
        status="success",
        records_processed=processed_count,
        failed_records=failed_count
    )
