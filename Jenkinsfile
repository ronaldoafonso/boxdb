pipeline {
    agent any
    environment {
        IMAGE_REPO = "ronaldoafonso"
        IMAGE_NAME = "boxdb"
        IMAGE_TAG = "0.0.11"
        IMAGE = "${IMAGE_REPO}/${IMAGE_NAME}:${IMAGE_TAG}"
    }
    stages {
        stage("Integration Tests") {
            steps {
                sh "docker-compose build boxdb-api "
                sh "docker-compose up --detach boxdb-mongo"
                sh "docker-compose up --detach boxdb-api"
                sh "docker-compose exec --detach --env BOXDB_MONGO=\$(docker-compose images | grep 'boxdb-mongo' | cut -d ' ' -f 1) boxdb-api bash -c 'python main.py'"
                sh "python3 -m venv venv"
                sh ". ./venv/bin/activate; pip install --no-cache-dir pytest==6.1.1 requests==2.24.0; pytest -xvvv"
                sh "docker image tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE}"
                sh "docker image push ${IMAGE}"
            }
        }
        stage("Stagging Tests") {
            steps {
                sh "minikube delete"
                sh "minikube start"
                sh "kubectl apply -f k8s/boxdb-namespace.yaml"
                sh "kubectl apply -f k8s/boxdb-secrets.yaml"
                sh "kubectl apply -f k8s/boxdb-pvs.yaml"
                sh "kubectl apply -f k8s/boxdb-pvcs.yaml"
                sh "kubectl apply -f k8s/boxdb-mongo-service.yaml"
                sh "kubectl apply -f k8s/boxdb-api-service.yaml"
                sh "kubectl apply -f k8s/boxdb-mongo-deployment.yaml"
                sh "kubectl apply -f k8s/boxdb-api-deployment.yaml"
                sh "./test/stagging.sh"
            }
        }
    }
    post {
        always {
            sh "docker-compose down"
            sh "minikube stop"
        }
    }
}
