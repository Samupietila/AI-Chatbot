pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'  // Virtual environment name
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub
                git branch: 'main', url: 'https://github.com/Samupietila/AI-Chatbot.git'
            }
        }

        stage('Setup') {
            steps {
                // Install dependencies and set up Python virtual environment
                  sh '''
                    python3 -m venv ${PYTHON_ENV}
                    source ${PYTHON_ENV}/bin/activate
                    pip install -r Flask-Website/requirements.txt
                '''
            }
        }
        
        /*stage('Test') {
            steps {
                // Run tests using pytest or unittest
                sh 'source ${PYTHON_ENV}/bin/activate && pytest Flask-Website/tests/'
            }
        }*/

        /*stage('Train Rasa model') {
            steps{
            sh 'source ${PYTHON_ENV}/bin/activate && rasa train --config Chatbot/config.yml --domain Chatbot/domain.yml --data Chatbot/data/'
            }
        }*/
        
       stage('Run rasa test') {
            steps{
                sh 'source ${PYTHON_ENV}/bin/activate && rasa test --stories Chatbot/data/stories.yml --nlu Chatbot/data/nlu.yml'
            }
        }
        /*stage('Run rasa tests with coverage') {
            steps{
                sh 'source ${PYTHON_ENV}/bin/activate && coverage run -m rasa test --stories data/stories.yml'
            }
            
        }*/
/*        stage('Run rasa tests with coverage') {
            steps{
                sh '''
                    source "${PYTHON_ENV}/bin/activate"
                    python3 -m coverage run -m rasa test --stories data/stories.yml
                    '''
            }
            
        }*/
        
        stage('Archive Test Artifacts') {
            steps {
                // Archive PNG files
                archiveArtifacts artifacts: '**/results/*.png', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/results/*.png', allowEmptyArchive: true
        }
    }
}