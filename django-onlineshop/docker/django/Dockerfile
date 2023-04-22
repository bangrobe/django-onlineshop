# pull official base image
FROM python:3.9.6-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# set work directory
WORKDIR /usr/src/app
# install psycopg2 dependencies
RUN apt-get update \
    && apt-get -y install netcat musl-dev python3-dev gcc postgresql postgresql-client libpq-dev \
    && apt-get clean

RUN apt-get update \
    && apt-get install -y binutils libproj-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]