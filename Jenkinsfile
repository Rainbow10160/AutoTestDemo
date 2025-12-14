pipeline {
    agent any
    
    stages {
        stage('1. 环境准备') {
            steps {
                script {
                    echo '正在安装依赖...'
                    
                    // 创建虚拟环境
                    sh 'python3 -m venv venv'
                    
                    // 激活虚拟环境并安装依赖
                    sh '''
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        
        stage('2. 执行测试') {
            steps {
                script {
                    // 在虚拟环境中运行测试
                    sh '''
                    source venv/bin/activate
                    pytest test_cases/ -v --alluredir=./allure-results
                    '''
                }
            }
        }
        
        stage('3. 生成报告') {
            steps {
                script {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: './allure-results']]
                    ])
                }
            }
        }
    }
}