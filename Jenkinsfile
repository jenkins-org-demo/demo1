pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                // Add build steps here
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Add test steps here
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! Deploying...'
            // Add deployment steps for successful builds
        }

        failure {
            echo 'Pipeline failed! Not deploying.'
            // Add actions for failed builds
        }
    }
}
