# Flask App Skeleton

Skeleton of a flask-based python app

## Local testing
Run using the development server, with:
```sh
$ python wsgi.py
```

Or with gunicorn:
```sh
$ gunicorn --bind='0.0.0.0:5000' wsgi:app
```

## Using Docker
Install and setup your docker environment.

Build the docker image with:
```sh
$ docker build -f deploy/Dockerfile -t server:latest .
```

And run with:
```sh
$ docker run -p 5000:5000 \
--network=host \
-e FLASK_APP=app \
-e FLASK_DEBUG=0 \
-e FLASK_ENV=<<ENVIRONMENT>> \
-e SQLALCHEMY_DATABASE_URI=<<DATABASE_URI>> \
-e SECRET_KEY=<<SECRET_KEY>> \
server:latest
```

