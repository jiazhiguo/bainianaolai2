import allure

from base.base_action import BaseAction
import page
# 类里面包含 点击首页 分类 购物车 我的
class HomePage(BaseAction):
    #初始化方法 动态传递driver
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step('点击我的')
    def click_btn_my(self):
        allure.attach('点击我的', '找到我的按钮实现点击')
        self.click_element(page.aolai_home_btn_my)

    



