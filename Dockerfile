FROM python:3
LABEL authors="cyber"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["flask", "--app", "app", "run", "--host", "0.0.0.0"]
