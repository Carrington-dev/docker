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
```docker re <image-name or id>```

## To restart existing images 
This will restart only existing stopped or running images
```docker restart <image-name or id>```
