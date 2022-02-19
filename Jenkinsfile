
pipeline{
    agent any

    stages{
        stage("A"){
            steps{
                echo "========executing A========"
            }
        }

        stage("B") {
            steps{
                echo "HOLAAA DESDE LA B"
            }
        }

        stage("C") {
            steps{
                echo "HOLAAA DESDE LA C"
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