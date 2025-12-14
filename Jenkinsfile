pipeline {
    agent {
        label 'master'  // 或你的节点标签
    }
    
    environment {
        // 使用绝对路径
        PYTHON = '/usr/bin/python3'
        PIP = '/usr/bin/pip3'
        VENV = "${WORKSPACE}/.venv"
    }
    
    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()  // 清理工作空间
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                script {
                    echo "Python 版本:"
                    sh "${PYTHON} --version"
                    
                    echo "创建虚拟环境..."
                    sh """
                    ${PYTHON} -m venv "${VENV}"
                    """
                    
                    echo "激活虚拟环境并安装依赖..."
                    sh """
                    . "${VENV}/bin/activate"
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    # 验证安装
                    pip list | grep -E "pytest|allure"
                    """
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    echo "运行测试..."
                    sh """
                    . "${VENV}/bin/activate"
                    # 设置项目路径
                    export PYTHONPATH="${WORKSPACE}:${PYTHONPATH}"
                    # 运行测试
                    python -m pytest test_cases/ \\
                        -v \\
                        --tb=short \\
                        --alluredir=allure-results \\
                        --junitxml=junit-results.xml
                    """
                }
            }
        }
        
        stage('Generate Report') {
            steps {
                script {
                    echo "生成测试报告..."
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']],
                        reportPath: 'allure-report'
                    ])
                    
                    // 同时保存 JUnit 报告
                    junit 'junit-results.xml'
                }
            }
        }
    }
    
    post {
        always {
            script {
                // 可选：保留虚拟环境用于调试
                if (currentBuild.currentResult == 'FAILURE') {
                    echo "构建失败，保留虚拟环境用于调试: ${VENV}"
                } else {
                    // 成功时清理
                    sh "rm -rf ${VENV}"
                }
                
                // 归档结果
                archiveArtifacts artifacts: 'allure-report/**', fingerprint: true
            }
        }
    }
}