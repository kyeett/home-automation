pipeline {
  agent any
  stages {
    stage('Commit made') {
      steps {
        echo 'Commit pushed'
      }
    }
    stage('Stuff completed') {
      steps {
        echo 'All done'
      }
    }
  }
  triggers {
    pollSCM('*/2 * * * *')
  }
}