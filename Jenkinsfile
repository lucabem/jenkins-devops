
pipeline{
    agent any

    stages{

        stage("Build"){
            steps{
                echo "========executing A========"
            }
        }

        stage("Test") {
            steps{
                echo "HOLAAA DESDE LA B"
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