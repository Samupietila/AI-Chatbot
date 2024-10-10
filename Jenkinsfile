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
                    if (isUnix()) {
                        // Check if Docker daemon is running for Unix-based systems
                        sh 'docker info > /dev/null 2>&1 || (echo "Docker daemon is not running" && exit 1)'
                        // Start MySQL container for Unix-based systems
                        sh """
                            docker run --name ${env.DB_CONTAINER_NAME} -e MYSQL_ROOT_PASSWORD=${env.DB_PASSWORD} -e MYSQL_DATABASE=${env.DB_NAME} -e MYSQL_USER=${env.DB_USER} -e MYSQL_PASSWORD=${env.DB_PASSWORD} -p ${env.DB_PORT}:3306 -d mysql:latest
                        """
                        // Wait for the database to be ready
                        sh 'sleep 30'
                    } else {
                        // Check if Docker daemon is running for Windows
                        bat 'docker info >nul 2>&1 || (echo Docker daemon is not running && exit 1)'
                        // Start MySQL container for Windows
                        bat """
                            docker run --name ${env.DB_CONTAINER_NAME} -e MYSQL_ROOT_PASSWORD=${env.DB_PASSWORD} -e MYSQL_DATABASE=${env.DB_NAME} -e MYSQL_USER=${env.DB_USER} -e MYSQL_PASSWORD=${env.DB_PASSWORD} -p ${env.DB_PORT}:3306 -d mysql:latest
                        """
                        // Wait for the database to be ready using ping
                        bat 'ping -n 30 127.0.0.1 > nul'
                    }
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    if (isUnix()) {
                        // Create the virtual environment for Unix-based systems
                        sh "python3 -m venv ${env.PYTHON_ENV}"
                    } else {
                        // Create the virtual environment for Windows
                        bat 'C:\\Users\\mika1\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m venv venv'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        // Activate the virtual environment and install dependencies for Unix-based systems
                        sh """
                            . ${env.PYTHON_ENV}/bin/activate
                            pip install --upgrade pip
                            pip install -r Flask-Website/requirements.txt
                        """
                    } else {
                        // Activate the virtual environment and install dependencies for Windows
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
            if (isUnix()) {
                // Create the reports directory if it doesn't exist and run tests for Unix-based systems
                sh """
                    mkdir -p reports
                    . ${env.PYTHON_ENV}/bin/activate
                    pytest Flask-Website/tests/ --junitxml=reports/results.xml || (echo "pytest failed" && exit 1)
                    ls -l reports  # List files in reports directory
                """
            } else {
                // Create the reports directory if it doesn't exist and run tests for Windows
                bat """
                    if not exist reports (mkdir reports)
                    ${env.PYTHON_ENV}\\Scripts\\activate
                    pytest Flask-Website\\tests\\ --junitxml=reports\\results.xml || (echo pytest failed && exit /b 1)
                    dir reports  # List files in reports directory
                """
            }
        }
    }
    post {
        always {
            // Archive test results
            junit '**/results.xml'
        }
    }
}

    }

    post {
        always {
            script {
                if (isUnix()) {
                    // Stop and remove the MySQL container for Unix-based systems
                    sh """
                        docker stop ${env.DB_CONTAINER_NAME}
                        docker rm ${env.DB_CONTAINER_NAME}
                    """
                } else {
                    // Stop and remove the MySQL container for Windows
                    bat """
                        docker stop ${env.DB_CONTAINER_NAME}
                        docker rm ${env.DB_CONTAINER_NAME}
                    """
                }
            }
            // Clean up the workspace
            cleanWs()
        }
    }
}
