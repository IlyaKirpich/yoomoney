FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

COPY cmd/app/main.py ./main.py
CMD ["python", "main.py"]