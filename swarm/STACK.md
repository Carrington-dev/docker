# Docker Stack

## Docker Swarm Visualizer
1. Install it tthrough docker compose because it's already avalable on the hub community
2. Chech your ip :8080
3. You can use this to visualize your workload on docker swarm.

## Installation steps

1. Write an approriate docker-compose.yml file for the visual
2. upload it to git
3. download it to your manager node
4. run the following on the correct directory

```bash
docker stack deploy -c docker-compose.yml visualizer_name
```

## Initializer Docker Swarm

```bash
docker info # to see if docker swarm is active
docker swarm init
docker swarm join-token manager
docker swarm join-token worker
```
## Docker Service
### To create a service

Services are basically containers running
```bash
docker service create <name>
```
### To rm a service

Services are basically containers running
```bash
docker service rm <service_id>
```
### To list all service

Services are basically containers running
```bash
docker service ls
```
### To list all containers in a servie

Services are basically containers running
```bash
docker service ls <service_id>
```

## Node
### Remove node from swarm

If it's not going down
```bash
docker node rm <node_id> --force
docker swarm leave # execute from the instance that has to leave
```

### Docker node promotion

1. To promote a node first find its id
```bash
docker node ls
```
2. Then use the id within the following command

```bash
docker node promote <node_id>
```

### To demote a node

1. To demote a node first find its id
```bash
docker node ls
```
2. Then use the id within the following command

```bash
docker node demote <node_id>
```

### Add/remove label to the node

1. To add node
```bash
docker node update --label-add <key>=<value> <node_id>
docker node update --label-add name=Carrington a6fjtk5
docker node inspect a6fjtk5
```

2. To remove node
```bash
docker node update --label-rm <key> <node_id>
docker node update --label-rm name a6fjtk5
docker node inspect a6fjtk5
```

## What happens if you you disconnect or switch off the manager node?

1. If you disconnect the manager the other node with many votes becomes the manager but the other disconnected manager can not join back if you switch it on.
2. The containers in a service will be redistributed according to the nodes lefts

## ps/ls commands

__Note that there are two confusing functions of note which are__

```bash
docker node ps
docker node ls
```
1. ls returns list of nodes in the swarm
2. ps returns list of containers in the node