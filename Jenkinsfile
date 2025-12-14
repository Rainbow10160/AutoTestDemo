pipeline {
    agent any

    // 关键点1：Mac上必须配置环境变量，否则Jenkins找不到 pip3 和 pytest
    environment {
        // /opt/homebrew/bin 是 M1/M2/M3 芯片的路径
        // /usr/local/bin 是 Intel 芯片的路径
        // 这样写可以同时兼容两种 Mac
        PATH = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:${env.PATH}"
        // 防止中文乱码
        PYTHONIOENCODING = "utf-8"
    }

    stages {
        stage('1. 环境准备') {
            steps {
                echo '正在安装依赖...'
                // Mac 上通常使用 pip3
                sh 'pip3 install -r requirements.txt'
            }
        }
        
        stage('2. 执行测试') {
            steps {
                echo '正在执行测试...'
                // 关键点2：Mac 支持 "|| true" 写法
                // 意思是：即使测试失败了，也要强行返回“成功”，好让流水线继续往下走去生成报告
                sh 'pytest --alluredir=./report/tmp || true'
            }
        }
    }

    post {
        always {
            echo '正在生成 Allure 报告...'
            // 关键点3：commandline: 'Allure2' 必须加！
            // 名字要和你 Jenkins 全局工具配置里的名字一模一样
            allure commandline: 'Allure2', includeProperties: false, jdk: '', results: [[path: 'report/tmp']]
        }
    }
}