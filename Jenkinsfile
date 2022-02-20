
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