## **Backend**
- **Python (Alpine)** → [python:3.12-alpine](https://hub.docker.com/_/python)
? We plan to use Py, but do we keep this version ?

? Need to decide if we are using a web server. Nginx might be best if we go with a server ?
## **Web Server**
- **Nginx** → [nginx:latest](https://hub.docker.com/_/nginx)

## **Database**
- **MongoDB** → [mongo:8.0.14-noble](https://hub.docker.com/_/mongo)

? Probably won't need a Cache ?
## **Cache**
- **Redis** → [redis:latest](https://hub.docker.com/_/redis)

## **Additional Dependencies**
- Any other dependencies can be listed here, such as Celery, Node.js, or worker services.
