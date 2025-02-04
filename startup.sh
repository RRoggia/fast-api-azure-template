# !/bin/bash
python -m gunicorn -k uvicorn.workers.UvicornWorker app.main:app
