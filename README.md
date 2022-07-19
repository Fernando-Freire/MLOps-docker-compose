# MLOps Deployment using Docker Compose
Easily deploy an MLflow tracking server for model registry and
a Feast Feature Store for feature tracking, both with docker-compose.

MinIO is used as the artifact store for MlFlow and offline store and registry for Feast.
MySQL server is used as the backend store for MLFlow.
Redis is used as online store for Feast.

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

The MLflow tracking server is composed of 5 docker containers:

* MLflow server
* Feast Web UI
* Redis key-value store
* MinIO object storage server
* MySQL database server

An addiotional Minio/mc container is run in order to set-up buckets.

## Origin

Based on the repo `https://github.com/sachua/mlflow-docker-compose.git`
