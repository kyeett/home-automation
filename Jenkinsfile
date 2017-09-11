pipeline {
  agent any
  triggers { pollSCM('*/2 * * * *') }
  stages {
    stage('Commit made') {
      steps {
        echo 'Commit pushed'
      }
    }
    stage('Test') {
      steps {
        sleep 1
        input 'Accept, dude!'
      }
    }
    stage('Stuff completed') {
      steps {
        echo 'All done'
      }
    }
  }
}