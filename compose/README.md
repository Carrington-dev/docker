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