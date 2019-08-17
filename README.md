# Flask Gunicorn

## Introduction

The architecture of the project is made using docker-compose, which manages to start backend (API) and Postgres containers.

## Development insights

It is used SQLAlchemy to manage objects in database and nodemon tool to allow us to write code and add it to docker container in real time.
Development time is being reduced and everything is run inside the final architecture, which reduces possible integration errors.

## Make the project

To start docker containers, just run:
```bash
docker-compose up
```

## Blueprints

### Score but not save in db
```bash
curl -X POST \
  http://localhost:8000/api/score \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: d984c6e7-d10d-41d3-9785-29ce281104fe' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F file=@<path_to_file>
```

### Score and save in db
```bash
curl -X POST \
  http://localhost:8000/api/score_save \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: d984c6e7-d10d-41d3-9785-29ce281104fe' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F file=@<path_to_file>
```