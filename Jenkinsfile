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
                git branch: 'Mikan-DB-Sekoilua', url: 'https://github.com/Samupietila/AI-Chatbot.git'
            }
        }

        stage('Setup Database') {
            steps {
                script {
                    if (isUnix()) {
                        // Check if Docker daemon is running for Unix-based systems
                        sh 'docker info > /dev/null 2>&1 || (echo "Docker daemon is not running" && exit 1)'
                        // Start MySQL container for Unix-based systems
                        sh 'docker run --name ${DB_CONTAINER_NAME} -e MYSQL_ROOT_PASSWORD=${DB_PASSWORD} -e MYSQL_DATABASE=${DB_NAME} -e MYSQL_USER=${DB_USER} -e MYSQL_PASSWORD=${DB_PASSWORD} -p ${DB_PORT}:${DB_PORT} -d mysql:latest'
                        // Wait for the database to be ready
                        sh 'sleep 30'
                    } else {
                        // Check if Docker daemon is running for Windows
                        bat 'docker info >nul 2>&1 || (echo Docker daemon is not running && exit 1)'
                        // Start MySQL container for Windows
                        bat 'docker run --name %DB_CONTAINER_NAME% -e MYSQL_ROOT_PASSWORD=%DB_PASSWORD% -e MYSQL_DATABASE=%DB_NAME% -e MYSQL_USER=%DB_USER% -e MYSQL_PASSWORD=%DB_PASSWORD% -p %DB_PORT%:%DB_PORT% -d mysql:latest'
                        // Wait for the database to be ready
                        bat 'ping -n 30 127.0.0.1 >nul'
                    }
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    if (isUnix()) {
                        // Create virtual environment for Unix-based systems
                        sh 'python3 -m venv ${PYTHON_ENV}'
                    } else {
                        // Create virtual environment for Windows
                        bat "C:\\Users\\mika1\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m venv venv"
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
                            . ${PYTHON_ENV}/bin/activate
                            pip install --upgrade pip
                            pip install -r Flask-Website/requirements.txt
                        """
                    } else {
                        // Activate the virtual environment and install dependencies for Windows
                        bat """
                            %PYTHON_ENV%\\Scripts\\activate
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
                            . ${PYTHON_ENV}/bin/activate
                            pytest Flask-Website/tests/ --junitxml=reports/results.xml || (echo "pytest failed" && exit 1)
                            ls -l reports  # List files in reports directory
                        """
                    } else {
                        // Create the reports directory if it doesn't exist and run tests for Windows
                        bat """
                            if not exist reports mkdir reports
                            %PYTHON_ENV%\\Scripts\\activate
                            pytest Flask-Website\\tests\\ --junitxml=reports\\results.xml || (echo pytest failed && exit /b 1)
                            dir reports  # List files in reports directory
                        """
                    }
                }
            }
        }
    }

    post {
        always {
            // Archive test results
            junit 'reports/results.xml'
            // Stop and remove the MySQL container
            script {
                if (isUnix()) {
                    sh 'docker stop ${DB_CONTAINER_NAME}'
                    sh 'docker rm ${DB_CONTAINER_NAME}'
                } else {
                    bat 'docker stop %DB_CONTAINER_NAME%'
                    bat 'docker rm %DB_CONTAINER_NAME%'
                }
            }
            // Clean up workspace
            cleanWs()
        }
    }
}
