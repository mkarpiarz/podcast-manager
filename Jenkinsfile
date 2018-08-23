#!/usr/bin/env groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                    additionalBuildArgs "-t app:${env.BUILD_ID}"
                }
            }
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image "app:${env.BUILD_ID}"
                    args '--link postgres:db -v jenkins-data:/var/jenkins_home'
                }
            }
            steps {
                echo 'Testing..'
                // The cwd here is the location the Docker plugin sets with the `-w` flag
                sh 'cd podcastmanager && python manage.py test'
            }
            post {
                always {
                    junit '**/podcastmanager/test_results/*.xml'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                wrap([$class: 'VaultBuildWrapper',
                    configuration: [vaultUrl: 'http://vault:8200',
                                    vaultCredentialId: 'vault'],
                    vaultSecrets: [
                        [path: 'kv/dockerhub',
                            secretValues: [
                                [envVar: 'DOCKER_USER', vaultKey: 'user'],
                                [envVar: 'DOCKER_PASS', vaultKey: 'pass']
                            ]
                        ]
                    ]
                ]) {
                    sh 'docker login --username $DOCKER_USER --password $DOCKER_PASS'
                    sh 'docker tag app:${BUILD_ID} $DOCKER_USER/app:latest'
                    sh 'docker push $DOCKER_USER/app:latest'
                }
            }
        }
    }
}
