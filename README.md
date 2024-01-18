# Docker tutorial for beginners

Docker is a containerized way of running different application with the same or different packages, tooks, source code without affecting one another in a same pc, instance or hypervisor. The docker run time will be the same for all of these docker images provided they are running on the same pc.

## Running the docker image
This is the first way to run a docker image
```bash
docker run -p <pc_port>:<docker_port> <docker_image_name>
docker run --publish <pc_port>:<docker_port> <docker_image_name>
```
The image above will stop if you click `ctrl + c` on your pc

__if you want to run a docker image in the background without interuption use the following command__

```bash
docker run -p -d <pc_port>:<docker_port> <docker_image_name>
docker run --publish --detach <pc_port>:<docker_port> <docker_image_name>
```
__Note that `-p = --publish` and `-d = --detach`__

Examples are given below

1.  Running a docker-nginx image
```bash
docker run -p -d 8000:80 nginx
```

2.  Running an apache web server
```bash
docker run -p -d 8000:80 apache
# could be wrong
```
3. Running custom images
```python
# will add more notes on this one
```

## List running containers
If you want to see all containers running in your pc use the following commands

```bash
dcoker containers ls # returns running containers
dcoker ls
dcoker ls -a
docker ps # this is an old way of doing it but it still works
```
`-a means all or irrespective of their status`

## To stop a container
if you a container is running in the image and you want to stop it use
```bash
docker container stop <container-id>
docker stop <container-id>
docker container stop <container-name>
docker stop <container-name>
docker container stop <container-first-four-charectors-on-id>
docker stop <container-first-four-charectors-on-id>
```

## Instances when a container is hidden
when an instance has been stopped it will be hidden to see it use
```docker ls -a```

## To search images on dockerhub

To search images on dockerhub 

```bash
docker search <image-name>
```

## To start existing images 
This will start only existing stopped images
```bash
docker start <image-name or id>
```

## To restart existing images 
This will restart only existing stopped or running images
```bash
docker restart <image-name or id>
```
## Defining a static container name

When running a container using `docker run` without providing a name for the container,dcker will create an assign a default name to that container `of some famous scientists` however if you want to assign a name for a container use '--name <name-you-want>'

e.g

```bash
docker run -p -d 8000:80 --name <name-you-want> nginx
docker run -p -d 8000:80 --name web_server nginx
```

To see the result of this use 

```bash
docker ps
docker ps -a
```

## To see problems or logs on a container

```bash
docker logs <container name>
```
## To see processes in a container

```bash
docker top <container-name> or < container-id>
```
also try this for all
```bash
ps -ef | grep <container-name>
ps -ef | grep nginx
```

## To remove or delete a container
__rm to running containers will give you an error__
```bash
docker rm <container-id>
docker rm <container-id> <...id2> <id3>
```

## Differences between Containers and Virtual Machines

1. They both have resource allocation and allocation benefits but the memory allocation for VMs is static where for containers it's static

2. Containers virtualizes operating systems where as VMs virtualizes hardware

3. Containers are more portable (1 creation multiple execution on different machines)

4. Containers are just processes

5. Contianers are limited to resources they can access

6. Containers can be killed on exit


## Execute a container with user supplied arguments

```bash
docker run --name custom-mysql -e MYSQL_ROOT_PASSWORD=#Mulalo96 -d mysql
```

## Docker Monitoring

### Resource Consuption Stats

```bash 
docker stats <container_name or container_id>
```
### Get detail information about a container (running)

Get a detailed information about docker container when running
```bash 
docker inspect <container_name or container_id>
```

## Execute the container in interactive mode

```bash
docker run -it <image_name> <commands>
```

-   using -i: means it will keep the stdin open if not attached
-   using -t: Allow a pseudo-TTY terminal open

examples 
```bash
docker run -it nginx /bin/bash # to access the terminal of the container
docker run -it nginx ls
docker run -it nginx pwd
```

__this works when launching only__


## Execute the bash commands on container that is already created

```bash
docker exec -it <image-name or id> touch /tmp/carrie
docker exec -it <image-name or id> /bin/bash
docker exec -it mysql_name mysql -uroot -p
```