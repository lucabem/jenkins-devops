
pipeline{
    
    agent {
      docker {
        image 'python'
      }
    }

    environment {
        HOME = "${env.WORKSPACE}"
    }

    stages{
        stage("GIT Checkout"){
            steps{
                checkout scm
            }
        }
        stage("Installing requirements"){
            steps{
                sh 'python -m pip install --user -r requirements.txt'
            }
        }
        stage("Testing") {
            steps{
                sh "python setup.py -q pytest"
            }
            post {
                success {
                    echo "Tests has been ended successfully - Well done!"
                }
                failure {
                    echo "There are some erros on tests - Try to solve them!"
                }
            }
        }

        stage("Deploy") {
            steps{
                echo "Here we will genereate the wheel"
                sh "touch Hey.txt"
            }
        }

        stage("Clean") {
            steps{
                cleanWs()
            }
        }
    }
}