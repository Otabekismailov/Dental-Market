# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#RUN apt update
#RUN apt-get install -y cron
#RUN alias py=python
#
#
#RUN apt-get update \
#  # dependencies for building Python packages
#  && apt-get install -y build-essential \
#  # psycopg2 dependencies
#  && apt-get install -y libpq-dev libmagic-dev \
#  # Translations dependencies
#  && apt-get install -y gettext \
#  # cleaning up unused files
#  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
#  && rm -rf /var/lib/apt/lists/*


# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /zygoma

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt





USER root

# (fyi) You can pass args from docker-compose.yml, just remove the "=myuser" from here
ARG USERNAME=myuser

# for whatever reason the /home/username directory is not created with useradd  for me :/
# RUN useradd -u ${USER_UID} --gid ${USER_GID} ${USERNAME}
RUN adduser --uid 1000 --disabled-password ${USERNAME}
# Install system dependencies

# Switch to our non-root user
USER ${USERNAME}
# add the default pip bin install location to the PATH
ENV PATH="$PATH:/home/${USERNAME}/.local/bin"
# Set the working directory to /app

WORKDIR /zygoma

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
#ARG UID=10001
#RUN adduser \
#    --disabled-password \
#    --gecos "" \
#    --home "/nonexistent" \
#    --shell "/sbin/nologin" \
#    --no-create-home \
#    --uid "${UID}" \
#    zygoma

# Copy the shell script into the container.
#COPY shell.sh /

# Set execution permissions for the shell script.
#RUN #chmod +x /shell.sh

# Switch to the non-privileged user to run the application.
#USER zygoma

# Copy the source code into the container.
COPY . .

# Set the entry point to execute the shell script.
#ENTRYPOINT ["/shell.sh"]

# Expose the port that the application listens on.
EXPOSE 8000

# Default command to run the application.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
