# MLOps Deployment using Docker Compose
Easily deploy an MLflow tracking server with docker-compose for model registry and
a Feast Feature Store for feature tracking.

MinIO S3 is used as the artifact store and MySQL server is used as the backend store.

Build and run the containers with `docker-compose`

    ```
    docker network cleate mlops
    chmod +x wait-for-it.sh
    docker-compose up -d --build
    ```

Access MLflow UI with http://localhost:5000
Access MinIO UI with http://localhost:9000
Access Feast UI with http://localhost:8888

## Containerization

The MLflow tracking server is composed of 3 docker containers:

* MLflow server
* Feast server
* Redis key-value store
* MinIO object storage server
* MySQL database server

An addiotional Minio/mc container is run in order to set-up buckets.

## Origin

Based on the repo `https://github.com/sachua/mlflow-docker-compose.git`
