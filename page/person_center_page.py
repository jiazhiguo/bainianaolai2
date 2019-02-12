import allure

from base.base_action import BaseAction
import page
class PersonCenterPage(BaseAction):
    #1.实现初始化方法
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step('个人中心设置')
    def click_btn_left_setting(self):
        allure.attach('个人中心页面', '点击左上角设置按钮')
        self.click_element(page.aolai_person_center_btn_left_setting)