# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11-slim-bookworm

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


# we move to the app folder and run the pip install command
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    cmake \
    curl 

# we copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install pip requirements
RUN pip install -r requirements.txt


# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 6769 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Download the CockroachDB root certificate into the container
ARG DB_CERT_URL
RUN curl --create-dirs -o $HOME/.postgresql/root.crt $DB_CERT_URL
# We copy the rest of the codebase into the image
COPY . /app

# We run the application
CMD ["python", "main.py"]