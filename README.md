# AMCEF test assignment

The project is containerized with docker and consists of 3 containers: MongoDB, Server and Frontend.

## Installation

You have to install these technologies:

* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)

After that just enter this command into terminal to initialize project (you have to be in root directory)

```bash
docker-compose up -d --build
```

Finally go to this [link](http://localhost:80/posts):

## Useful commands

Stop project:

```bash
docker-compose stop
```

Start project:

```bash
docker-compose start
```

Remove all containers:

```bash
docker-compose down
```

## Swagger documentations
* [Server](http://localhost:8001/docs)

* [Frontend](http://localhost:80/docs)

## Container ports
* MongoDB - 8000
* Server - 8001
* Frontend - 80

## List of things what I have done
* Jinja2 API with Template Inheritance included
* Bootstrap as a front-end framework
* Responsive web design
* Client-side validation (*title*, *body*)
* Server-side validation (*userId*)
* ORM with pymongo
* Use of external API for *userId* validation when creating new post
* Error handling
* Project containerization


## List of things what I haven't done (was not able to figure out)
* Hide error message in create post page when *userId* is correct but title or body are not valid