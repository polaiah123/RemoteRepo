pipeline {
    agent any

    stages {
        stage('Commit') {
            steps {
                echo 'Commit is done'
            }
        }
         stage('Build') {
            steps {
                
                echo "The build ID of this job is ${BUILD_ID}"

            }
        }
         stage('Test') {
            steps {
              echo "The build URL is ${BUILD_URL}"
            }
        }
         stage('Stage') {
            steps {
                echo 'Staging is done'
            }
        }
         stage('Deploy') {
            steps {
                echo 'Deployment is done'
            }
        }
    }
}
