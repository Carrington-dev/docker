# Docker tutorial for beginners

Docker is a containerized way of running different application with the same or different packages, tooks, source code without affecting one another in a same pc, instance or hypervisor. The docker run time will be the same for all of these docker images provided they are running on the same pc.

# Docker basics

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
# docker run -it --name mysql_name -e MYSQL_ROOT_PASSWORD=#Mulalo96 mysql -uroot -p
docker run -it --name mysql_client -e MYSQL_ROOT_PASSWORD=#Mulalo96 mysql
```

## To stop all containers

```
docker stop $(docker ps -a -q)

```
## To remove all containers

```bash
docker rm $(docker ps -a -q)
docker container prune # all stopped containers
docker image prune # not tagged latest

```

## Useful commands for Docker
Before I leave you, I have prepared a list of commands that may be useful to you on Docker.

### List your images.
```bash
docker image ls
```
### Delete a specific image.
```bash
docker image rm [image name]
```
### Delete all existing images.
```
docker image rm $(docker images -a -q)
```
### List all existing containers (running and not running).
```bash
docker ps -a
```
### Stop a specific container.
```bash
docker stop [container name]
```
### Stop all running containers.
```bash
docker stop $(docker ps -a -q)
```
### Delete a specific container (only if stopped).
```bash
docker rm [container name]
```
### Delete all containers (only if stopped).
```bash
docker rm $(docker ps -a -q)
```
### Display logs of a container.
```bash
docker logs [container name]
```

# Docker networks

if you want to connect two instances/containers to run on the same network interface then this is the way.

Networks connects a container to another container and two containers to a host machine

## Bridge Network

By default all docker containers are connected to the bridge network which is th default network created by the runtime envrionment. All containers in the bridge network communicate with each other using ip-addresses.Containers on different host machine cannot communicate with each other without additional configuration

## Overlay Network

This model enables communication between containers from two or more different host machines. Technlogies like VXLAN or IPSec are often used to create virtual machines that span multiple hosts.

## Container Network Interfaces 

CNI is a specification that defines how a container runtime interacts with networking plugins. it allows different container runtimes to be combined with various networking solutions.

## To find port of a container

```
docker port <contianer_id>
docker port <contianer_name>
```

## Find docker container ip

```
docker inspect <contianer_id or name>
```
filter one item
```bash
docker inspect <container_id> -f {{ .key.value }}
```

## Docker Network CLI Commands

1.  to see all networks are available
```bash
docker network ls
```
2. to create a network

```
dcoker network create my_bridge_net
```

## To filter networks

To filter networks in the bridge
```bash
docker network -f drive=bridge

```

To finds all networks ids and drivers

```bash
docker network ls -f "{{ .ID }}: {{ .Driver }}"
```

Try 
```bash
docker network --help
```

## Docker DNS (Domain Name System)

DNS is a system in which domains to thier respective ip addresses

Dontainers use DNS to communicate

__can add network to container when run using --network <network_name>__

check if containers in the same network are connected

```bash

docker run -it <container1> ping <container_2>

```

