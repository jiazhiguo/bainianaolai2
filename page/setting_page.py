import allure

from base.base_action import BaseAction
import page
import time
class SettingPage(BaseAction):
    #1.初始化函数
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step('退出登录')
    def click_setting_btn_logout(self):
        allure.attach('退出登录', '实现向上滑动')
        self.swipe_screen(1)
        time.sleep(1)
        allure.attach('退出登录', '点击退出按钮')
        self.click_element(page.aolai_setting_btn_setting_logout)
        allure.attach('退出登录', '点击对话框确认按钮')
        self.click_element(page.aolai_setting_btn_dialog_confirm)

