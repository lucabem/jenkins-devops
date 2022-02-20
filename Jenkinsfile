
pipeline{
    
    agent {
      docker {
        image 'python:3'
        label 'my-build-agent'
      }
    }

    stages{

        stage("Build"){
            steps{
                echo "========executing A========"
                sh "python --version"
            }
        }

        stage("Test") {
            steps{
                echo "Executing main.py to test"

                sh "python main.py"
            }
        }

        stage("Deploy") {
            steps{
                sh 'ls -l'
            }
        }

    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}