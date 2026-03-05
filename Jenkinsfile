pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // This pulls the code from your GitHub repo
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Preparing the environment...'
                // You could install dependencies here: sh 'pip install -r requirements.txt'
                sh 'python3 --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                // This runs our test script
                sh 'python3 tester_worker.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application (Simulation)...'
                sh 'python3 worker.py'
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up workspace...'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}
