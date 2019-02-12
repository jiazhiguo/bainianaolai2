import allure

from base.base_action import BaseAction
import page
class RegistPage(BaseAction):
    #1.初始化函数 传递driver
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step('点击已有账号')
    def click_btn_already_account(self):
        allure.attach('点击已有账号', '找到已有账号实现点击')
        self.click_element(page.aolai_regist_btn_already_account)
   