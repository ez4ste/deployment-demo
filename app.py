"""Deployment Demo — FastAPI health-check service."""

import os
from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel

app = FastAPI(title="deployment-demo")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    uptime: str
    timestamp: str
    hostname: str


@app.get("/health", response_model=HealthResponse)
def health():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        service="deployment-demo",
        version=os.getenv("APP_VERSION", "0.0.0"),
        uptime=datetime.now(timezone.utc).isoformat(),
        timestamp=datetime.now(timezone.utc).isoformat(),
        hostname=os.getenv("HOSTNAME", "unknown"),
    )


@app.get("/")
def root():
    """Root endpoint."""
    return {
        "message": "deployment-demo is running",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/ui", response_class=HTMLResponse)
def ui():
    """Serve the dashboard UI."""
    return FileResponse(os.path.join(BASE_DIR, "static", "index.html"))
