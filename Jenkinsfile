pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'  // Virtual environment name
        DB_CONTAINER_NAME = 'test-mysql'
        DB_PORT = '3306'
        DB_USER = 'testuser'
        DB_PASSWORD = 'testpassword'
        DB_NAME = 'testdb'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub
                git branch: 'main', url: 'https://github.com/Samupietila/AI-Chatbot.git'
            }
        }

        stage('Setup Database') {
            steps {
                script {
                    // Start MySQL container
                    sh """
                        docker run --name ${env.DB_CONTAINER_NAME} -e MYSQL_ROOT_PASSWORD=${env.DB_PASSWORD} -e MYSQL_DATABASE=${env.DB_NAME} -e MYSQL_USER=${env.DB_USER} -e MYSQL_PASSWORD=${env.DB_PASSWORD} -p ${env.DB_PORT}:3306 -d mysql:latest
                    """
                    // Wait for the database to be ready
                    sh 'sleep 30'
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Create the virtual environment
                    if (isUnix()) {
                        sh "python3 -m venv ${env.PYTHON_ENV}"
                    } else {
                        bat "python -m venv ${env.PYTHON_ENV}"
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Activate the virtual environment and install dependencies
                    if (isUnix()) {
                        sh """
                            . ${env.PYTHON_ENV}/bin/activate
                            pip install --upgrade pip
                            pip install -r Flask-Website/requirements.txt
                        """
                    } else {
                        bat """
                            ${env.PYTHON_ENV}\\Scripts\\activate
                            pip install --upgrade pip
                            pip install -r Flask-Website\\requirements.txt
                        """
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Activate the virtual environment and run tests
                    if (isUnix()) {
                        sh """
                            . ${env.PYTHON_ENV}/bin/activate
                            pytest Flask-Website/tests/ --junitxml=reports/results.xml
                        """
                    } else {
                        bat """
                            ${env.PYTHON_ENV}\\Scripts\\activate
                            pytest Flask-Website\\tests\\ --junitxml=reports\\results.xml
                        """
                    }
                }
            }
            post {
                always {
                    // Archive test results
                    junit 'reports/results.xml'
                }
            }
        }
    }

    post {
        always {
            // Stop and remove the MySQL container
            sh """
                docker stop ${env.DB_CONTAINER_NAME}
                docker rm ${env.DB_CONTAINER_NAME}
            """
            // Clean up the workspace
            cleanWs()
        }
    }
}