import pytest
from utils.logger import log

@pytest.fixture(scope="session", autouse=True)
def setup_session():
    log.info("=== 自动化测试项目开始运行 ===")
    yield
    log.info("=== 自动化测试项目运行结束 ===")

@pytest.fixture(scope="function")
def login_fixture():
    log.info(">> 前置操作：正在执行登录...")
    # 这里模拟登录逻辑
    token = "fake_token_12345"
    yield token  # 把token传给测试用例
    log.info(">> 后置操作：清理数据/退出登录")