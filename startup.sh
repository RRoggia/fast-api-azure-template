# !/bin/bash
source .venv/bin/activate
python -m gunicorn -k uvicorn.workers.UvicornWorker app.main:app
