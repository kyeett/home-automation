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
        parallel(
          "Test": {
            sleep 1
            input 'Accept, dude!'
            
          },
          "Test 2": {
            mail(subject: 'Commit pushed', body: 'Commit pushed. Already told you that.', from: 'jenkins@jenkins.com', to: 'magnus.wahlstrand@gmail.com')
            
          }
        )
      }
    }
    stage('Stuff completed') {
      steps {
        echo 'All done'
      }
    }
  }
}