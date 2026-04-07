#!/usr/bin/env python3
"""Deployment Demo — FastAPI health-check service."""

import os
from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="deployment-demo")


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
