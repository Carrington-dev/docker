# Introduction:

Docker Swarm is a powerful clustering and orchestration tool that allows you to manage and scale Docker containers across multiple nodes. In this guide, we will cover the basics of Docker Swarm, including setting up a Swarm, joining nodes, deploying services, scaling, updating, and more. Whether you’re new to Docker or looking to expand your container orchestration skills, this article will provide you with a solid foundation to get started with Docker Swarm.

For a visual demonstration of these steps, you can check out this YouTube video tutorial: https://youtu.be/w8vCq2u_qh8

## Prerequisites:

Before we dive into Docker Swarm, ensure you have the following:
- A basic understanding of Docker concepts and commands.
- Three machines (virtual or physical): one as the manager node and two as worker nodes. These machines should have Docker installed.

## Setting Up Docker Swarm:

### Initialize the Swarm on the manager node:
```bash

docker swarm init - advertise-addr <MANAGER_NODE_IP>
```
2. Join the worker nodes to the Swarm:
On each worker node, run the following command (replace <MANAGER_NODE_IP> with the IP address of the manager node):
```bash
docker swarm join - token <TOKEN> <MANAGER_NODE_IP>:2377
```
3. Verify the Swarm status:
On the manager node, run:
```bash
docker node ls
```
Deploying and Managing Services in Docker Swarm:

##  Deploying a service:
```bash
docker service create - name my-nginx - replicas 3 -p 80:80 nginx
```
Listing services:
```bash
docker service ls
```
## Scaling a service:
```bash
docker service scale my-nginx=5
```
## Updating a service:
```bash
docker service update - image nginx:latest my-nginx
```
## Inspecting a service:
```bash
docker service inspect my-nginx
```
## Removing a service:
```bash
docker service rm my-nginx
```
## Conclusion:

Docker Swarm provides a simple yet powerful solution for orchestrating containers in a distributed environment. With the ability to deploy, scale, update, and manage services across multiple nodes, Docker Swarm empowers developers and system administrators to build resilient and scalable applications.

Remember to experiment and explore additional features such as service rolling updates, service rollback, service constraints, and more. Happy container orchestration with Docker Swarm!

References:
- https://docs.docker.com/engine/swarm/
- https://docs.docker.com/