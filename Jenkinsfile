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
                // TODO: push image to DockerHub
            }
        }
    }
}
