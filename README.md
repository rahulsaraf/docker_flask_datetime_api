# DateTime API Server

### Requirements -
Expose three APIs that take JSON input via GET requests, and return JSON output

* A date API that returns the current date
* A time API that returns the current time
* A datetime API that returns the current date and time

Should be containerized web service exposing three public APIs accessible on localhost (port 8080).

### Project structure -

```
project name: ploysign_api_task
    /polysign_api_task
        /api
            __init__.py
            api_classes.py
            api_endpoints.py
         app.py
         Dockerfile
         readme.md
         requirements.txt
```

##### api_classes.py - 
    This file contains logic of creating request and response for each endpoint.
##### api_endpoints.py - 
    This file contains code for each endpoint.

### Dockerfile -
```
FROM python:3.5
COPY . /app
WORKDIR /app
ENV FLASK_APP=app.py
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
```

### How to run -
```
cd polysign_api_task
docker build -t polysign_api_image .
docker run -d --name polysign_task -p 8080:8080 polysign_api_image

#check if process is running
docker ps 

#curl to test
docker exec -it polysign_task curl -X GET -H "Content-Type: application/json" -d '{"full":"true"}' http://localhost:8080/date
docker exec -it polysign_task curl -X GET -H "Content-Type: application/json" -d '{"full":"false"}' http://localhost:8080/date
docker exec -it polysign_task curl -X GET -H "Content-Type: application/json" http://localhost:8080/date

docker exec -it polysign_task curl -X GET -H "Content-Type: application/json" -d '{"military":"true",full":"true"}' http://localhost:8080/time
docker exec -it polysign_task curl -X GET -H "Content-Type: application/json" -d '{"military":"true","full":"false"}' http://localhost:8080/time
docker exec -it polysign_task curl -X GET -H "Content-Type: application/json" -d '{"military":"false",full":"true"}' http://localhost:8080/time
docker exec -it polysign_task curl -X GET -H "Content-Type: application/json" -d '{"military":"false","full":"false"}' http://localhost:8080/time
docker exec -it polysign_task curl -X GET -H "Content-Type: application/json" -d '{"full":"true"}' http://localhost:8080/time
docker exec -it polysign_task curl -X GET -H "Content-Type: application/json" -d '{"military":"true"}' http://localhost:8080/time
docker exec -it polysign_task curl -X GET -H "Content-Type: application/json" http://localhost:8080/time

docker exec -it polysign_task curl -X GET -H "Content-Type: application/json" -d '{"date":{"full":"true"},time":{military":"true",full":"true"}}' http://localhost:8080/datetime
docker exec -it polysign_task curl -X GET -H "Content-Type: application/json" -d '{"date":{"full":"false"},time":{military":"false",full":"true"}}' http://localhost:8080/datetime
docker exec -it polysign_task curl -X GET -H "Content-Type: application/json" http://localhost:8080/datetime

docker rm $(docker ps -a -q)
docker rmi $(docker images -q)

```
