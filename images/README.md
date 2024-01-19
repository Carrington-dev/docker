# Docker images

A combination of file systems, and parameters. Images contain dependencies and binaries needed to run or xecute the application.

Images contain the data which is required to execute the containers.

## List images

```bash
docker images
```

Alphine is the base image which you can create as your base image.

### Docker Central Repository

dockerhub a place where you can find all images


### To download images

```
docker pull <image_name>
```

to pull by specific tag

```
docker pull <image_name>:<tag>
```

## Docker Image Layers

- Each image consists of a series of layers. Docker makes use of union file systems to combine these layers into one image.

- Union file systems all files and directories of seperate file systems known as branches

- to see the image layers downloaded

```
docker history mysql:<tag>
```

Each step when building a Dockerfile is a layer

__Note: When pull docker images it compares the similar available downloaded images with the one you are looking for and only updates the new layer.__

## Docker Image Tagging
- Docker tags are tags which you associate which your image
- They are basically the versions of your images
- tags are added during building of images
- tags this way
```bash
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
```

This way we can tag images local
```bash
docker tag wordpress:2.3.1 my_word_press:4.5.1
```
## Docker Image Uploading

hub.docker.com
```bash
docker login
```

to push follow this method

```
docker image push <username>/<image_name>
```

## Dockerfile

-   Docker automatically builds images by reading the Dockerfile 
-   A dockerfile is document that contains all instructions needed to create an image
-   A dockerfile may contain read-only layers each of which represents a docker instruction
-   Command to build an image from dockerfile
```bash
docker build -f <path_of_file>
```

### Dockerfile Instructions
A set of instructions in dockerfile
#### FROM
```bash
FROM

```
#### LABEL

-   Used to give license to the user
-   Used to add information about the image

```Dockerfile
LABEL user="Carrington <from@stemgon.co.za>"

```
#### RUN
-   RUN will execute a new layer on top of the basic command

```Dockerfile
RUN apt-get update

```
#### CMD
```Dockerfile
# Used to run instruction contained by the image along with it's arguementa
CMD ['<instrion>', <arguments-1>, <second-arguments>]

```

__There can only one CMD instruction in the file__

CMD is usually the last instruction in the Dockerfile

#### EXPOSE

Used to expose any PORT

```Dockerfile
# Used to run instruction contained by the image along with it's arguementa
EXPOSE <PORT>
```
#### ENV

ENV sets environment variables to their values

#### ADD
add files to a specific directory in the image

```Dockerfile
# Used to run instruction contained by the image along with it's arguementa
ADD /home/* /home/destination/
```
#### VOLUME
-   Used to expose any database storage area, configuration storage, or files/folders created by your docker container

#### WORKDIR

-   tells the working directory for RUN, CMD, ADD

#### COPY

same as ADD but can take urls


## Build Dockerfiles

```Dokcerfile
docker build -t <image_name>:<tage> dir
<!-- -t = tags -->
```

## 