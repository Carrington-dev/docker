# Docker tutorial for beginners

Docker is a containerized way of running different application with the same or different packages, tooks, source code without affecting one another in a same pc, instance or hypervisor. The docker run time will be the same for all of these docker images provided they are running on the same pc.

## Running the docker image
This is the first way to run a docker image
```
docker run -p <pc_port>:<docker_port> <docker_image_name>
docker run --publish <pc_port>:<docker_port> <docker_image_name>
```
The image above will stop if you click `ctrl + c` on your pc

__if you want to run a docker image in the background without interuption use the following command__

```
docker run -p -d <pc_port>:<docker_port> <docker_image_name>
docker run --publish --detach <pc_port>:<docker_port> <docker_image_name>
```
__Note that -p = --publish and -d = --detach__

Examples are given below

1.  Running a docker-nginx image

2.  Running an apache web server