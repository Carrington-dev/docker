# How to manage secrets in docker swarm

```bash
docker secret --help
```

## To create a secret
### By File

```bash
docker secret create <secret_name> <secret_file>
```
### By CLI

```bash
echo "Secret_value" > docker secret create <secret_name> -
```

## To list out

```bash
dcoker secret ls
```

## To inspect secret

```bash
dcoker secret <secret_name>
```

