# Web Stack Debugging 0

This project is part of the Holberton School curriculum and is focused on debugging web servers. The goal is to fix an Apache web server running inside a Docker container so that it returns a web page containing "Hello Holberton" when queried at the root.

## Prerequisites

Before you begin, make sure you have Docker installed. You can follow the Docker installation guide for your specific operating system:

- [Docker for Mac](https://docs.docker.com/docker-for-mac/install/)
- [Docker for Windows](https://docs.docker.com/docker-for-windows/install/)
- [Docker for Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/holberton-system_engineering-devops.git
   ```

2. Navigate to the project directory:

   ```bash
   cd holberton-system_engineering-devops/0x0D-web_stack_debugging_0
   ```

3. Start the Docker container with Apache and port mapping:

   ```bash
   docker run -p 8080:80 -d -it holbertonschool/265-0
   ```

4. Check if the container is running:

   ```bash
   docker ps
   ```

   You should see an output similar to this:

   ```
   CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
   47ca3994a491        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla
   ```

## Debugging

The container is running, but when you try to access it using `curl`, you get an empty reply from the server:

```bash
curl 0:8080
curl: (52) Empty reply from server
```

Your task is to connect to the container and fix the issue so that it returns the expected "Hello Holberton" message.

1. Connect to the Docker container using `docker exec`:

   ```bash
   docker exec -it CONTAINER_ID /bin/bash
   ```

   Replace `CONTAINER_ID` with the actual ID of your running container.

2. Inside the container, investigate the Apache web server configuration and identify the issue that prevents it from serving the web page correctly.

3. Fix the issue. You may need to check Apache's configuration files, make adjustments, or install missing packages.

4. Once you have fixed the problem, exit the container.

## Verification

After exiting the container, you can verify that the web server is working correctly by running:

```bash
curl 0:8080
```

You should see the following output:

```bash
Hello Holberton
```

## Solution

Paste the command(s) you used to fix the issue in the `0-give_me_a_page` file.
