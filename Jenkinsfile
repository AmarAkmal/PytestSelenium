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
        sh 'cd operations && python -m pytest -v -s --alluredir=test_login.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }    
    }
  }
}
