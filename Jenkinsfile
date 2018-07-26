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
                    args '--link postgres:db'
                }
            }
            steps {
                echo 'Testing..'
                sh 'cd /opt/project && python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                // TODO: push image to DockerHub
            }
        }
    }
}
