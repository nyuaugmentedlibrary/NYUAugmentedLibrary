FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/backend

COPY requirements.txt /app/backend/

# Build psycopg2-binary from source -- add required required dependencies
RUN apk add --virtual .build-deps --no-cache postgresql-dev gcc python3-dev musl-dev && \
        pip install --upgrade setuptools && \
        pip install --no-cache-dir -r requirements.txt && \
        apk --purge del .build-deps




COPY backend /app/backend/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

#We start with a base image set variables PYTHONUNBUFFERED and PYTHONDONTWRITEBYTECODE to 1 for logging and not creation of .pyc files respectively.
#Set the working directory inside the container to /app/backend/ for the backend.
#Copy the requirements file to the working directory and install the requirements.
#Install required dependencies for building the psycopg2-binary from source
#Copy the content of our backend to the docker container
#The starting command for our container