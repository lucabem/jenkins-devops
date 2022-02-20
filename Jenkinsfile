
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
        stage("Installing requirements"){
            steps{
                sh 'python -m pip install --user -r requirements.txt'
            }
        }

        stage("Testing") {
            steps{
                sh "python setup.py -q pytest"
            }
        }

        stage("Deploy") {
            steps{
                sh 'ls -l'
            }
        }

    }
    post{
        success{
            echo "Everythin has been correctly - Well done!"
        }
        failure{
            echo "Pipeline has failed"
        }
    }
}