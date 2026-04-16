pipeline {
    agent any
    stages {
        stage('Checkout (Ingredientes)') {
            steps {
                echo 'Descargando el código...'
                checkout scm
            }
        }
        stage('Build (Cocinar)') {
            steps {
                echo 'Cocinando la imagen Docker...'
                sh 'docker build -t burgercode-app .'
            }
        }
        stage('Test (Control de Calidad)') {
            steps {
                echo 'Ejecutando PyBuilder...'
                sh 'docker run --rm burgercode-app pyb'
            }
        }
        stage('Deploy (Entrega)') {
            steps {
                echo 'Desplegando en puerto seguro...'
                sh 'docker rm -f burger-prod || true'
                sh 'docker run -d --name burger-prod -p 8443:5000 burgercode-app'
                echo '¡App desplegada en http://localhost:8443!'
            }
        }
    }
    post {
        always {
            echo 'Limpiando la cocina...'
            sh 'docker image prune -f'
        }
        success {
            echo '🎉 ¡Pipeline completado con éxito!'
        }
        failure {
            echo '🚑 ¡ALERTA! El pipeline ha fallado. Revisar logs.'
        }
    }
}
