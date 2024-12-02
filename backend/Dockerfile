FROM python:3.12-slim-bookworm

WORKDIR /app

# Install system updates and security patches
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    sqlite3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir \
    flask==3.0.0 \
    flask-cors==4.0.0 \
    flask-sqlalchemy==3.1.1 \
    python-dotenv==1.0.0 \
    gunicorn==21.2.0 \
    starlette==0.31.1

COPY . .

EXPOSE 5000

# Run with gunicorn for better security and performance
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "flask_app.app:app"]
