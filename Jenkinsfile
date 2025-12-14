pipeline {
    agent any
    
    environment {
        // 项目特定环境变量
        PROJECT_DIR = "${WORKSPACE}"
        VENV_PATH = "${PROJECT_DIR}/venv"
        // 某些系统可能需要指定字符集避免中文乱码
        LANG = "C.UTF-8"
    }
    
    stages {
        stage('1. 检查环境') {
            steps {
                script {
                    echo "工作目录: ${WORKSPACE}"
                    // 检查机器上是否安装了 python3
                    sh 'python3 --version' 
                }
            }
        }
        
        stage('2. 创建虚拟环境') {
            steps {
                script {
                    echo '正在重建虚拟环境...'
                    sh '''
                    # 如果存在则删除，保证环境纯净
                    if [ -d "venv" ]; then
                        rm -rf venv
                    fi
                    python3 -m venv venv
                    '''
                }
            }
        }
        
        stage('3. 安装依赖') {
            steps {
                script {
                    echo '正在安装依赖...'
                    sh '''
                    # 注意：在 Jenkins sh 中，source 必须和命令在同一个 block 里
                    . venv/bin/activate
                    pip install --upgrade pip
                    
                    if [ -f "requirements.txt" ]; then
                        pip install -r requirements.txt
                    else
                        echo "警告：未找到 requirements.txt"
                    fi
                    '''
                }
            }
        }
        
        stage('4. 执行测试') {
            steps {
                script {
                    echo '正在执行测试...'
                    sh '''
                    . venv/bin/activate
                    export PYTHONPATH="${WORKSPACE}:$PYTHONPATH"
                    
                    # 运行测试 (加上 || true 确保即使测试失败，流水线也能继续执行去生成报告)
                    pytest test_cases/ -v --alluredir=./allure-results || true
                    '''
                }
            }
        }
        
        stage('5. 生成报告') {
            steps {
                script {
                    echo '正在生成 Allure 报告...'
                    // 确保你的 Jenkins 已经安装 Allure 插件并在"全局工具配置"中配置了 Allure Commandline
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
            script {
                // 如果是 failure，发送通知等操作可以在这里做
                if (currentBuild.currentResult == 'FAILURE') {
                    echo "构建检测到失败，请检查测试报告。"
                }
            }
        }
        cleanup {
            // 构建完成后清理工作空间，节省磁盘
            cleanWs()
        }
    }
}