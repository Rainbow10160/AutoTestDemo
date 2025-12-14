# test_jenkins_local.sh
#!/bin/bash
echo "模拟 Jenkins 环境运行..."

# 创建临时目录模拟 Jenkins workspace
TEST_DIR="/tmp/jenkins_test_$(date +%s)"
mkdir -p "$TEST_DIR"
cp -r . "$TEST_DIR/"
cd "$TEST_DIR"

echo "工作目录: $TEST_DIR"
echo

# 执行类似 Jenkins 的步骤
echo "1. 创建虚拟环境..."
python3 -m venv venv
source venv/bin/activate

echo "2. 安装依赖..."
pip install -r requirements.txt

echo "3. 设置环境变量..."
export PYTHONPATH="$TEST_DIR:$PYTHONPATH"

echo "4. 运行测试..."
pytest test_cases/ -v --alluredir=./allure-results

echo "5. 生成报告..."
if [ -d "allure-results" ]; then
    allure generate allure-results -o allure-report --clean
    echo "报告生成在: $TEST_DIR/allure-report"
else
    echo "警告: 没有测试结果生成"
fi

echo
echo "测试完成！"
echo "清理: rm -rf $TEST_DIR"