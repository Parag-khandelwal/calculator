pipeline {
    agent any

    environment {
        // Set Python environment path
        PYTHON_ENV = "C:\\Users\\khand\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"   // Adjust based on where Python is installed
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone the Git repository
                git branch: 'main', url: 'https://github.com/Parag-khandelwal/calculator.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies (assuming requirements.txt)
                bat """
                ${PYTHON_ENV} -m pip install --upgrade pip
                ${PYTHON_ENV} -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                // Run unit tests using unittest
                bat """
                ${PYTHON_ENV} -m unittest discover tests
                """
            }
        }

        stage("build") {
            bat """
            echo "Running the calculator app"
            python .\\src\\calculator.py
            echo "Successfully executed the application"
            """
        }
    }

    post {
        always {
            // Clean workspace after the job is done
            cleanWs()
        }
    }
}
