import pytest
import allure
from utils.logger import log

@allure.feature("用户登录模块")
class TestLogin:

    @allure.story("正常登录测试")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success(self, login_fixture):
        log.info(f"获取到的Token: {login_fixture}")
        
        with allure.step("步骤1：输入用户名"):
            log.info("输入用户名: admin_V2_自动触发测试")
        
        with allure.step("步骤2：输入密码"):
            log.info("输入密码: *****")
            
        with allure.step("步骤3：点击登录"):
            log.info("点击登录按钮")
        
        assert "success" == "success"
        log.info("断言成功：登录跳转正常")

    @allure.story("密码错误测试")
    def test_login_fail(self):
        log.info("正在执行密码错误测试")
        with allure.step("输入错误密码"):
            pass
        # 故意写个失败的断言，看看Allure里红色的效果
        assert 1 + 1 == 3