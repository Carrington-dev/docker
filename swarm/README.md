# Docker swarm tutorial

## Important commands

## Free online docker swarm

```bash
play-with-docker
```

## To see all nodes

On the manager node
```
docker node ps
```

## Create docker swarm cluster

1. Install docker
2. Add docker to user-group
3. 

## To get help

```bash
docker node --help
```

## To get a token at runtime

```bash
docker swarm join-token manager
docker swarm join-token worker
```

## To switch manager node in docker

```bash
docker node update --role manager <node_name>
```

## To see

```bash
docker node ls
```

## To join new node to the swarm
1. create a token

```bash
docker swarm join-token worker
```

2. copy the out an execute to the node you would like to join

## To promote a node

```bash
docker node promote <any_manager>
```

## To create a service in docker swarm

Concept
```bash
docker service create --replicas <number_of_replicas> <image> <command>
```
Examples
```bash
docker service create --replicas 10 alpine ping www.stemgon.co.za
```
To see all services or containers running
```bash
docker service ps <service_name>
```

## To verify which services are running

```bash
docker services ps <service_name> # which containers
```

## Visualizing the workload on the docker cluster

1. install docker swarm visualizer
    We will 
2. 