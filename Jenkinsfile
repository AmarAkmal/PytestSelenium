pipeline {
  agent { docker { 
		image 'python:3.7.6' 
		args '-u root:root'
	} 
  }
  stages {
    stage('build') {
      steps {
          sh "pip install --user -r requirements.txt"
      }
    }
    stage('test') {
      steps {
        sh 'python test.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }    
    }
  }
}
