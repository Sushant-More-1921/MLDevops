
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\Sushant More\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Code successfully pulled from GitHub'
            }
        }

        stage('Verify Python') {
            steps {
                bat '"%PYTHON%" --version'
                bat '"%PYTHON%" -m pip --version'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                bat '"%PYTHON%" -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v --junitxml=pytest-results.xml'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat '.venv\\Scripts\\python.exe monitoring.py'
            }
        }
    }

    post {
        always {
            junit(
                testResults: 'pytest-results.xml',
                allowEmptyResults: true
            )

            archiveArtifacts(
                artifacts: 'evidently_report.html,pytest-results.xml',
                allowEmptyArchive: true
            )
        }
    }
}
