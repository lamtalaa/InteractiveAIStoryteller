web: uvicorn main:app --host 0.0.0.0 --port 10000
web: gunicorn -w 4 -b 0.0.0.0:$PORT frontend:app