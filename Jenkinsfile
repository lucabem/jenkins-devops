
pipeline{
    
    agent {
      docker {
        image 'python'
      }
    }

    options { skipDefaultCheckout() }

    environment {
        HOME = "${env.WORKSPACE}"
        SBX_EMAIL_USER = credentials('ce941911-858b-44db-a1de-c2b190f07d85')
        DEV_EMAIL_USER = credentials('fdcf878f-065d-4063-bada-2f76dd211024	')
    }

    parameters {
        string(name: 'TAG', defaultValue: '', description: 'Version')
        choice(name: 'CHOICES', choices: ['calidad', 'estructuras', 'estructura_con_notas', 'impacto_prioridad', 'linaje', 'administracion'],
                description: 'Select collection to deploy')
        string(name: 'ids', defaultValue: 'all', description: 'IDs (separated by , without spaces -> 1,2,3)')
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
                echo "Global property file: ${SBX_EMAIL_USER_USR}"
                echo "Global property file: ${SBX_EMAIL_USER_PSW}"

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