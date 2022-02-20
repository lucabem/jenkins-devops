
pipeline{
    
    agent {
      docker {
        image 'python'
      }
    }

    stages{

        stage("Build"){
            steps{
                sh "Installing requirementes for building model..."
                sh "pip install -r  requirements.txt"
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