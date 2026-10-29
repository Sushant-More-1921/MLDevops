
pipeline {
    agent any

    stages {
        stage('Setup Python') {
            steps {
                bat 'python --version'
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
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
