pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'pipenv install --dev'
      }
    }
    stage('Code Linting') {
      steps {
        sh 'pass'
      }
    }
    stage('Test') {
      steps {
        sh 'pass'
      }
    }
    stage('Deploy') {
      steps {
        sh 'pass'
      }
    }
  }
}