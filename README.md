# deployment-demo

Demo FastAPI service deployed via agent-driven GitHub Actions pipeline.

## Endpoints
- `/` — Root info
- `/health` — Health check with status, version, hostname
- `/docs` — OpenAPI docs (automatic)

## Deploy
Push to `main` → Actions runs lint, test, deploy to Hetzner VPS via SSH.
