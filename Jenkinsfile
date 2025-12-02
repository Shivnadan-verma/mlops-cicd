pipeline {
    agent any

    environment {
        JFROG_REGISTRY = "trialok42lr.jfrog.io"
        DOCKER_REPO = "ml-docker-local"
        IMAGE_NAME = "ml-fastapi"
        IMAGE_TAG = "v${env.BUILD_NUMBER}"
        FULL_IMAGE = "${JFROG_REGISTRY}/${DOCKER_REPO}/${IMAGE_NAME}:${IMAGE_TAG}"
        KUBECONFIG = "${env.HOME}/.kube/config"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Train ML Model') {
            steps {
                echo "Training ML model..."
                sh """
                python train_model.py
                ls -l
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${FULL_IMAGE}"
                sh """
                docker build -t ${FULL_IMAGE} .
                """
            }
        }

        stage('Login to JFrog Registry') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'jfrog-cred',
                                                 usernameVariable: 'JF_USER',
                                                 passwordVariable: 'JF_PASS')]) {
                    sh """
                    echo "$JF_PASS" | docker login ${JFROG_REGISTRY} -u "$JF_USER" --password-stdin
                    """
                }
            }
        }

        stage('Push Image to JFrog') {
            steps {
                sh """
                docker push ${FULL_IMAGE}
                """
            }
        }

        stage('Deploy to EKS (Rolling Update)') {
            steps {
                echo "Rolling update on EKS..."
                sh """
                kubectl set image deployment/fastapi-ml fastapi-ml=${FULL_IMAGE} --record
                kubectl rollout status deployment/fastapi-ml
                """
            }
        }

        stage('Verify Deployment') {
            steps {
                sh """
                kubectl get pods -l app=fastapi-ml
                kubectl get svc fastapi-ml-service
                """
            }
        }
    }

    post {
        failure {
            echo "Pipeline failed. Check logs."
        }
        success {
            echo "CI/CD completed successfully. Deployed image: ${FULL_IMAGE}"
        }
    }
}
