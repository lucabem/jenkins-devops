
pipeline{
    
    agent {
      docker {
        image 'python'
      }
    }

    stages{
        stage("Installing requirements"){
            steps{
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python -m pip install --user -r requirements.txt'
                }
            }
        }

        stage("Testing") {
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