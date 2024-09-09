pipeline {
    agent any

    environment {
        PYTHON_ENV = "C:\\Users\\khand\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"   
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Parag-khandelwal/calculator.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                ${PYTHON_ENV} -m pip install --upgrade pip
                ${PYTHON_ENV} -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                ${PYTHON_ENV} -m unittest discover tests
                """
            }
        }

    }

    post {
        always {
            cleanWs()
        }
    }
}
