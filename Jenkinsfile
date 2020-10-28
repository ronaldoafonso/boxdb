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
            }
        }
    }
}
