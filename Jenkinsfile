pipeline {
    agent any
    triggers {
        githubPush() // This line enables the GitHub push trigger
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building...' // this line is a test
            }
        }
    }
}
