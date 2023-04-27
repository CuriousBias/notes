## Docker
- Popular service for packaging, deploying, and running distributed and cloud native applications. 
- Easy to automate infrastructure, isolate applications, maintain consistence and improve resource utilization.
- Open source solution with enterprise tier. 

### Architecture
- Client-server architecture and a remote API
- Docker Image: template/recipe for creating docker containers. Includes steps for installing and running software.
- Docker Container: Virtual machine running on docker host. 
- Docker Client: Command-line utility to use Docker API
- Docker Host: Physical or virtual machine running Docker daemon.
- Docker Registry: A repository  of Docker images. Docker Hub (https://hub.docker.com is most popular).
- Docker Machine: Utility to manage multiple Docker hosts (either local or remote).
- Docker Daemon:

### Running a Container:
1. Install Docker
2. Run a container: Containers run from command line. 

```
docker run -rm hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.
```
To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.(amd64)
 3. The Docker daemon created a new container from that image which runs the executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it to your terminal.

### Workflow
1. Build image from Dockerfile (2 ways)
    1. Pull image from registry
        1. Visit any repository. 
        2. Pull docker image (ex “mysql”)
            1. Pull latest mysql docker image ```% docker pull mysql```
            2. Pull specific version ```% docker pull mysql:8.0.1```
    2. Build image from Dockerfile
        1. In file “Dockerfile” inherit from mysql and then run a command. 
        ```
        FROM mysql:5.5.45
        RUN echo <command>
        ```

        2. Build docker image and provide a name to image (-t) ```% docker build -t est-mysql .```
        3. View images ```% docker images```
2. Run the image to create container as runtime environment.
    1. Run docker image ```% docker run —name my-container -d -e VAR_A=var -e VAR_B=var_b -p 3306:3306```
        - specific environment variables (-e) 
        - for long running processes like daemons (-d)
        - Add a container name (—name)
        - Map ports as necessary (-p)
        - remove container after execution and reclaim space (—rm)

    2. See running containers, images they were created from, the command run, any ports that software is listening, and container name ```% docker ps```
    3. Find IP for docker container ```% docker-machine ip default```
3. Stopping and starting containers
    - Stop: ```% docker stop my-container```
    - Start ```% docker start my-container```

### Networking Containers
- Docker automatically creates 3 networks. Will need to create a custom network.
- View current docker networks ```% docker network ls```
- Create user-defined network ```% docker network create my-network```
- Add container to network 
- After container startup```% docker network connect my-network my-container```
- During container startup with network (—network) ```% docker run —rm my-image —network my-network```

### Mapping Volumes
In order to share directories between running container and host machine. To ensure data files persist and are backed up on host machine. 
```% docker run —name my-image -v /my/host/datadir:/var/lib/```

### Tagging an Image
Tag to add username, image name, and version number. ```% docker tag my-image username/image_name/version```

### Push image to repository
1. Create Docker Hub account at https://hub.docker.com 
2. Login to docker with username and password ```% docker login```
3. Push image ```docker push username/my-image/version

### Other helpful Commands
- List containers ```% docker ps -a```
- Remove images ```% docker rm my-image```
- List ports (3306 for MySQL or 80 for web server) ```% docker port my-container```
- List processes in a container ```% docker top my-container```
- Execute commands in a running container ```% docker exec my-container ls```

### Dockerfile
- Primary way of creating an image
- Instructions for installing and configuring software.
- Any files in same directory will be used for build process. 
- Use .dockerignore file to exclude any files
- comments start with # character
- Instructions executed in order of docker file

### Dockerfile Instructions
```
FROM: This must be the first instruction in the Dockerfile and identifies the image to inherit from.
MAINTAINER: Provides visibility and credit to the author of the image
RUN: Executes a Linux command for configuring and installing
ENTRYPOINT: The final script or application used  to bootstrap the container, making it an executable application
CMD: Provide default arguments to the ENTRYPOINT using a JSON array format
LABEL: Name/value metadata about the image
ENV: Sets environment variables
COPY: Copies files into the container
ADD: Alternative to copy
WORKDIR: Sets working directory for RUN, CMD, ENTRYPOINT, COPY, and/or ADD instructions
EXPOSE: Ports the container will listen on
VOLUME: Creates a mount point
USER: User to run RUN, CMD, and/or ENTRYPOINT instructions
```

### Docker Machine
- Command line utility used to manage local or remote hosts.
- “default” is created when installing Docker Toolbox
- Local machines: VirtualBox instances
- Remote machines: hosted on AWS, etc

#### Commands
- List machines ```% docker-machine ls```
- Create machine ```% docker-machine create -d virtualbox my-machine```
- Start machine ```% docker-machine start my-machine```
- Stop machine  ```% docker-machine stop my-machine```
