FROM python:3.11.0a7-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        ffmpeg \
        openalpr \
        dos2unix
RUN apt-get clean

# Install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "src/controller.py" ]