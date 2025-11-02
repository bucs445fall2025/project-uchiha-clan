# Dockerfile for app

FROM python:3.12-alpine

WORKDIR /app/
EXPOSE 5000

# Run alpine dependencies
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev

# Copy requirements.txt file
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
