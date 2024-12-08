FROM python:3.13-alpine3.20
LABEL authors="Skandar"
WORKDIR /usr/app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt;

COPY src ./src

COPY main.py main.py

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]