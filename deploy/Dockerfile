FROM python:3.6.3-alpine3.6

WORKDIR /opt/server

RUN apk update \
    && apk add libpq postgresql-dev \
    && apk add build-base

COPY requirements.txt /opt/server/requirements.txt

# Installing and build python module
RUN pip install -r requirements.txt

COPY . /opt/server

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "--chdir=/opt/server", "wsgi:app"]


