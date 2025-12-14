# 在项目根目录创建 check_requirements.sh
#!/bin/bash
echo "=== 检查依赖安装 ==="

# 创建临时虚拟环境测试
python3 -m venv test_venv
source test_venv/bin/activate

echo "1. 安装依赖..."
pip install -r requirements.txt

echo "2. 测试导入..."
python3 -c "
try:
    import pytest
    import allure
    print('✅ 核心依赖安装成功')
except ImportError as e:
    print(f'❌ 导入失败: {e}')

# 测试项目特定导入
import sys
sys.path.insert(0, '.')
try:
    from utils.logger import log
    print('✅ 项目模块导入成功')
except ImportError as e:
    print(f'❌ 项目模块导入失败: {e}')
"

deactivate
rm -rf test_venv