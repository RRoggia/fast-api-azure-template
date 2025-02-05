# !/bin/bash
source .venv/bin/activate
python -m uvicorn --log-level trace --reload app.main:app
