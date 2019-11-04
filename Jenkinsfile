pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''pipenv install --dev'''
        // telegramSend '🍎vbetGameResult -- Build'
      }
    }
    // stage('Test') {
    //   steps {
    //     telegramSend '🍎vbetGameResult -- Test'
    //   sh '''pipenv run pytest -vv'''
    //   }
    // }
    stage('Deploy') {
      steps {
        // telegramSend '🍎vbetGameResult -- Deploy'
        ansiblePlaybook(
          playbook: 'deploy.yml',
          inventory: 'hosts',
          credentialsId: '5b754041-7e6b-49d7-91a4-676aeb8dc6c5'
        )
      }
    }
  }
  post {
    // success {
    //     telegramSend '🍎vbetGameResult -- 🙆‍'
    // }
    // failure {
    //     telegramSend '🍎vbetGameResult -- 🙅‍'
    // }
    cleanup {
      sh 'pipenv --rm'
    }
  }
}


// step 1
// 把本機鑰匙放到jenkins
// step 2
// 把目標機器鑰匙放到git
// 即可連動機器