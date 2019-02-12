import allure

from base.base_action import BaseAction
import page
class LoginPage(BaseAction):
    #1.初始化方法
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step('测试登录')
    def click_btn_login(self,username,password):
        allure.attach('登录', '输入账号')
        self.input_edit_content(page.aolai_login_edit_account,username)
        allure.attach('登录', '输入密码')
        self.input_edit_content(page.aolai_login_edit_password,password)
        allure.attach('登录', '点击登录按钮')
        self.click_element(page.aolai_login_btn_login)

    #3 点击关闭登录页面的功能
    def click_close_login_page(self):
        self.click_element(page.aolai_login_btn_close_login)

