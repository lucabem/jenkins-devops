
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
        string(name: 'TAG', defaultValue: '', description: 'Version')
        choice(name: 'CHOICES', choices: ['calidad', 'estructuras', 'estructura_con_notas', 'impacto_prioridad', 'linaje', 'administracion'],
                description: 'Select collection to deploy')
        string(name: 'ids', defaultValue: 'all', description: 'IDs (separated by , example 1, 2, 3)')
    }

    stages{
        stage("GIT Checkout"){
            steps{
                script {
                    if (params.TAG != '') {
                        checkout scm: [$class: 'GitSCM',
                            userRemoteConfigs: [[
                                url: 'https://github.com/lucabem/jenkins-devops',
                                credentialsId: 'a337f278-706f-43a0-b97f-ffe30de2036e'
                            ]], 
                            branches: [[name: 'refs/tags/${TAG}']]], 
                            poll: false
                    } else {
                       checkout scm
                    }
                }
            }
        }

        stage("Setting up"){
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
                sh "python main.py ${params.CHOICES} ${params.ids}"
            }
        }

        stage("Clean") {
            steps{
                cleanWs()
            }
        }
    }
}