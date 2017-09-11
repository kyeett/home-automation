pipeline {
  agent any
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