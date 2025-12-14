pipeline {
    agent any
    
    tools {
        // 在 Jenkins 中配置的 Python
        python "Python3"  // 需要在 Jenkins 全局工具配置中定义
    }
    
    environment {
        // 项目特定环境变量
        PROJECT_DIR = "${WORKSPACE}"
        VENV_PATH = "${PROJECT_DIR}/venv"
    }
    
    stages {
        stage('1. 检查环境') {
            steps {
                script {
                    echo "工作目录: ${WORKSPACE}"
                    sh 'python3 --version'
                    sh 'pip3 --version'
                }
            }
        }
        
        stage('2. 创建虚拟环境') {
            steps {
                script {
                    echo '正在创建虚拟环境...'
                    sh '''
                    # 删除旧的虚拟环境
                    rm -rf venv
                    # 创建新的虚拟环境
                    python3 -m venv venv
                    # 验证
                    ls -la venv/bin/python
                    '''
                }
            }
        }
        
        stage('3. 安装依赖') {
            steps {
                script {
                    echo '正在安装依赖...'
                    sh '''
                    # 激活虚拟环境
                    source venv/bin/activate
                    # 升级 pip
                    pip install --upgrade pip
                    # 安装依赖
                    pip install -r requirements.txt
                    # 列出已安装的包
                    pip list
                    '''
                }
            }
        }
        
        stage('4. 执行测试') {
            steps {
                script {
                    echo '正在执行测试...'
                    sh '''
                    # 激活虚拟环境
                    source venv/bin/activate
                    # 设置 PYTHONPATH
                    export PYTHONPATH="${WORKSPACE}:$PYTHONPATH"
                    # 运行测试
                    pytest test_cases/ -v --alluredir=./allure-results
                    '''
                }
            }
        }
        
        stage('5. 生成报告') {
            steps {
                script {
                    echo '正在生成 Allure 报告...'
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
    
    post {
        always {
            echo '清理工作空间...'
            // 可选：保留虚拟环境
            // sh 'rm -rf venv'
            
            // 生成汇总报告
            script {
                def currentResult = currentBuild.currentResult
                if (currentResult == 'FAILURE') {
                    echo "构建失败！"
                } else {
                    echo "构建成功！"
                }
            }
        }
    }
}