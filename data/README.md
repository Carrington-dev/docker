# Data Problems

-   Docker containers are immutable meaning if you install python 3.8 for instance you cannot upgrade to 3.9 rather you need to repackage a new conainer for these requirements.

-   Data inside containers is lost once the container is redeployed and to cater for this we will use two possible solutions.

## Data Volumes

-   Volumes are another way to store persistance container data for a docker container outside of the container in the host file systems which is controled by docker. 

-   Volumes are easily accessible even when the container is stopped, once it's started again it will be visible

```bash
docker volume ps -a
docker volume ls -a
```

You can also inspect the data volume using the commands below

```bash
docker volume inspect <volume-id>
```

## Data Mount

-   meaning a file or directory in the host machine is mounted to the continaer
-   this means the host file systsem is mapped to the container file system
-   bound mount can be store anywhere in the host machine
-   Non-docker host on the machine can alter files at any time
-   Data mounts can not be used in the dockerfile

### Use cases of this

-   can be used to share configurations beteen host machine and container files
-   sharing development source code 

### Starting nginx with bind mounds

```
docker container run -d --name nginx --mount type=bind source=$(pwd),target=/app nginx
```

You can test it by checking your desktop file system andyour app file system
