pipeline {
    agent any
    stages {
        stage("Integration Tests") {
            steps {
                sh "docker-compose up --detach --build"
                sh "docker-compose exec --detach boxdb-api bash -c 'python main.py'"
                sh "python -m venv venv"
                sh "source venv/bin/activate; pip install --no-cache-dir pytest==6.1.1 requests==2.24.0; pytest -vvv"
                sh "docker-compose down"
                sh "docker image tag boxdb:0.0.9 ronaldoafonso/boxdb:0.0.9"
                sh "docker image push ronaldoafonso/boxdb:0.0.9"
            }
        }
        stage("Stagging Tests") {
            steps {
                sh "kubectl apply -f k8s/boxdb-namespace.yaml"
                sh "kubectl apply -f k8s/boxdb-configmap.yaml"
                sh "kubectl apply -f k8s/boxdb-mongo-service.yaml"
                sh "kubectl apply -f k8s/boxdb-api-service.yaml"
                sh "kubectl apply -f k8s/boxdb-mongo-deployment.yaml"
                sh "kubectl apply -f k8s/boxdb-api-deployment.yaml"
            }
        }
    }
}
