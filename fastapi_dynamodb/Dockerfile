FROM python:3.8-slim
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
ENV PORT 6969

CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT}