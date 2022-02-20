
pipeline{
    
    agent {
      docker {
        image 'python'
      }
    }

    stages{

        stage("Build"){
            steps{
                sh "whoami"
                echo "Installing requirementes for building model..."
                sh "python -m pip install -r requirements.txt"
            }
        }

        stage("Test") {
            steps{
                sh "python setup.py pytest"
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