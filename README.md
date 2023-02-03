# Install Typesense
In this guide, we’ll install Typesense using Docker.
For other methods of installation, refer to Typesense the official website: https://typesense.org/docs/guide/install-typesense.html

## Docker
Pull the Typesense docker image with the following command:

```
docker pull typesense/typesense:0.23.1
```

### Start Typesense from the Docker image
**Docker on  Mac / Linux**

To get started with Typesense using docker on Mac / Linux, run the following commands: 
```
export TYPESENSE_API_KEY=xyz

mkdir $(pwd)/typesense-data

docker run -p 8108:8108 -v$(pwd)/typesense-data:/data typesense/typesense:0.23.1 \
  --data-dir /data --api-key=$TYPESENSE_API_KEY --enable-cors
```

**Docker on  Windows**

To get started with Typesense using docker on Windows, run the following commands: 

```
set TYPESENSE_API_KEY=xyz

mkdir typesense-data

docker run -p 8108:8108 -v/typesense-data:/data typesense/typesense:0.23.1 --data-dir /data --api-key=$TYPESENSE_API_KEY --enable-cors
```

## Healthcheck
You can use the /health API end-point to verify that the server is ready to accept requests.

```
curl http://localhost:8108/health
# Expected response: {"ok":true}
```

# Run a local Typesense server with Docker Compose

eg. `docker-compose.yml`:
```
version: "3"

services:
    typesense:
        container_name: typesense-server
        image: typesense/typesense:0.24.0
        environment: # configure typesense server using environment variables
            TYPESENSE_DATA_DIR: /data
            TYPESENSE_ENABLE_CORS: true
            TYPESENSE_API_KEY: xyz
        ports:
            - 8108:8108
        volumes:
            - /typesense-data:/data # /typesense-data is used to store search engine data
```

To start the service (in detached mode):
```
docker compose up -d
```

To check whether the server is running:
```
curl http://localhost:8108/health
# Expected response: {"ok":true}
```

To stop the service:
```
docker compose down
```

To stop the service and delete the volume:

**NOTE: This will delete all your Typesense data**
```
docker compose down --volumes
```
