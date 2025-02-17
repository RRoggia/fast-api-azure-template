# !/bin/bash
python -m uvicorn --port 8000 --host 0.0.0.0 app.main:app
