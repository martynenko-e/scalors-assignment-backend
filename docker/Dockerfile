# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

ARG APP_ENV=dev
ENV APP_ENV ${APP_ENV}

# Install pip requirements
ADD ./requirements /app/requirements
RUN python -m pip install -r /app/requirements/${APP_ENV}.txt

WORKDIR /app
ADD ./src /app

ADD ./docker/entrypoint.${APP_ENV}.sh /entrypoint.sh

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

ENTRYPOINT [ "bash", "/entrypoint.sh" ]
