# Docker compose 

- A tool for running and building multicontainer applications
- It allows you to define the stack in a docker-compose.yaml file
- It has a version of the docker-compose.yaml file

## Docker Compose Basics
- It is written in YAML file format, hence it is important to under this format
- It is a combination of key and values
- It is composed of indentation as python (use space)

Maps

### To build 

```bash
docker-compose build
```
### To execute 

```bash
docker-compose up
```
### To terminate 

```bash
docker-compose down
```

## Key Concepts of a docker-compose.yml file

1. Version
2. Services
    - Each service has a parameter called name

```docker-compose

services:
    web:
        image: nginx:latest
        ports:
            - "80:80"

```
3. Volumes
    - allows you to define your volume and bind mount for persistant data

```docker-compose

volumes:
    data-volume:

```

4. Networks
- Can define custom networks ad connect them to the instance

```
networks:
    custom-network:

```

5. Environmental variables

You can set the environment keys for your services


```
environment:
    - MODE_ENV=production

```
This is a list

6. Ports

```
ports:
    - "80:80"
```

7. Command


```compose
command: npm start
```

8. Building docker images

- Workflow of building images in docker-compose

- __Docker workflow__

Docker file -> Docker build command -> Docker image

- __Build images in docker-compose workflow__

    - ``docker-compose build``
    - ``docker compose build``


- Docker-compose build properties
- build/context: defines the path or git location where your docker is located

```
build:
    context: ./dir
```
```
services:
    webapp:
        build: <git-url>
```

10. Image

    - This overides the dockerfile name e.g 
    ```
    services:
        webapp:
            build:
                context: .
                dockerfile: Dockerfile.dev
            image: custom-image-name:tag
    ```

11. Dockerfile
    - it specifiles the alternative dockerfile to build

12. args
    - Passes the build arguments to the build context at runtime. Using for dynamically setting the env_values during build

    ```
    ARG GIT_COMMIT
    RUN echo "This is my git url ${GIT_COMMIT}"
    ```

    ```
    build:
        context: .
        args: 
            GIT_COMMIT: hfhtkslf-df
    ```

    it may also look like this

    ```
     build:
        context: .
        args: 
           - GIT_COMMIT: hfhtkslf-df
    ```

13. Tags
    - it defines the set of tags you want to associate with your builds
    