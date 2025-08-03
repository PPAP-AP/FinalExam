FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y postgresql-client
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x wait-for-postgres.sh

CMD ["./wait-for-postgres.sh", "python", "app.py"]

