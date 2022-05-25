FROM python:3.8-slim

COPY . .

RUN pip install -r requirements.txt

CMD uvicorn app:app --host 127.0.0.1 --port 8000