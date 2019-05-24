# Flask App Skeleton

Skeleton of a flask-based python app, that uses the port `8080`.

## Local testing
Run using the development server, with:
```sh
$ python server.py
```
Or with gunicorn:
```sh
$ gunicorn --bind='0.0.0.0:8080' server:app
```

## Using Google App Engine
Download SDK from https://cloud.google.com/sdk/ and setup your environment.

Test locally with:
```sh
$ dev_appserver.py app.yaml
```

Or deploy to the cloud with:
```sh
$ gcloud app deploy
```

