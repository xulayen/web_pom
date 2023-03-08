import allure
import pytest


class Test_register():
    @pytest.fixture(autouse=True)
    def openbrow(self, register):
        register.open('/users/register/')
    #
    # @pytest.fixture()
    # def delete_sq(self,db1):
    #     sql='delete from xxx where xxx=""'
    #     db1.excute(sql)
    #

    @allure.step("测试注册功能")
    @allure.severity('block')
    @pytest.mark.parametrize('eval,p',[('123@qq.com','123456'),('youyou@qq.com','123456')],ids=['测试用例1','测试用例2'])
    def test_email1(self,register,eval,p):
        allure.dynamic.description('注册功能')
        with allure.step("先清空名称输入框"):
            register.clear_nameloc()
        with allure.step("先清空密码输入框"):
            register.clear_pasloc()
        with allure.step("输入邮箱"):
            register.input_email(eval)
        with allure.step("输入密码"):
            register.input_password(p)
        with allure.step("点击登录按钮"):
            register.click_register()
