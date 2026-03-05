pipeline {
    // We replaced 'agent any' with this specific block
    agent {
        docker { 
            // This tells Podman to download a clean, isolated Python environment
            image 'python:3.9-slim' 
            
            // This is often needed so Jenkins has permission to read/write inside the container
            args '-u root'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Preparing the environment...'
                sh 'python3 --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
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
