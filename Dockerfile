FROM ubuntu:16.04

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
# The 3 openalpr packages and libopenalpr-dev depend SPECIFICALLY on ubuntu:16.04!
# If there is a need to update the base image, those packages might not work.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libssl-dev \
        libffi-dev \
        ffmpeg \
        python3-setuptools \
        python3-pip \
        python3-dev \
        openalpr \
        openalpr-daemon \
        openalpr-utils \
        libopenalpr-dev \
    && apt-get upgrade -y \
    && apt-get autoremove \
    && apt-get clean

# Install the newest version of python (This is needed due to it using ubuntu:16.04 as image)
RUN apt install software-properties-common -y \
    && add-apt-repository -y ppa:jblgf0/python\
    && apt-get update \
    && apt-get install python3.7 -y

# Install python dependencies
RUN python3.7 -m pip install --upgrade pip
COPY ./requirements.txt .
RUN python3.7 -m pip install -r requirements.txt

# Copy everything inside the /alpr folder into the docker container
COPY ./src ./src

CMD [ "python3.7", "src/controller.py" ]