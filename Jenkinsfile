
pipeline{
    
    agent {
      docker {
        image 'python'
      }
    }

    options { skipDefaultCheckout() }

    environment {
        HOME = "${env.WORKSPACE}"
    }

    parameters {
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
        text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some information about the person')
        booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')
        choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')
        password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
    }

    stages{
        stage("GIT Checkout"){
            steps{
                checkout scm
            }
        }

        stage('Example') {
            steps {
                echo "Hello ${params.PERSON}"
                echo "Biography: ${params.BIOGRAPHY}"
                echo "Toggle: ${params.TOGGLE}"
                echo "Choice: ${params.CHOICE}"
                echo "Password: ${params.PASSWORD}"
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