# Flask App Skeleton

Skeleton of a flask-based python app

## Local testing
Run using the development server, with:
```sh
$ python server.py
```
Or with gunicorn:
```sh
$ gunicorn --bind='0.0.0.0:8080' server:app
```

## Deploy using Google App Engine
Download SDK from https://cloud.google.com/sdk/ and setup your environment.

Test locally with:
```sh
$ dev_appserver.py app.yaml
```

Or deploy to the cloud with:
```sh
$ gcloud app deploy
```

## Using Docker
Install and setup your docker environment.

Build the docker image with:
```sh
$ docker build -f deploy/Dockerfile -t server:latest .
```

And run with:
```sh
$ docker run -d -p 8080:8080 server:latest
```

