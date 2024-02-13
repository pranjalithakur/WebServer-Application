This folder contains the Docker configuration for setting up a web server environment with an Nginx reverse proxy and Selenium for security testing.

# Structure

- `Dockerfile`: Docker configuration file to build the web server image.
- `docker-compose.yml`: Defines the services, networks, and volumes for the Docker environment.
- `nginx.conf`: Configuration file for the Nginx reverse proxy.
- `Code/`: Directory containing web server code and static files.

# Dependencies
```bash
sudo apt install docker docker-compose docker.io
```

# Usage
```bash
sudo docker-compose up --build
```
