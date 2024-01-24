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