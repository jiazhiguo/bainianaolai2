import allure

import page
from base.base_action import BaseAction


class AddressPage(BaseAction):



    def __init__(self,driver):
        super().__init__(driver)

    @allure.step('点击设置')
    def click_setting_btn(self):
        allure.attach('点击设置', '找到设置按钮实现点击')
        self.click_element(page.aolao_setting_btn)

    @allure.step('点击地址管理')
    def click_address_manager_btn(self):
        allure.attach('点击地址管理', '找到地址管理按钮实现点击')
        self.click_element(page.aolao_address_manager)

    @allure.step('点击新增地址')
    def click_add_address_btn(self):
        allure.attach('点击新增地址', '找到新增地址按钮实现点击')
        self.click_element(page.aolao_add_address)

    @allure.step('输入收件人')
    def input_addressee(self,addressee):
        allure.attach('输入收件人', '输入收件人')
        self.input_edit_content(page.aolai_addressee,addressee)

    @allure.step('输入手机号')
    def input_tel(self,tel):
        allure.attach('输入手机号', '输入手机号')
        self.input_edit_content(page.aolai_tel, tel)

    @allure.step('选择所在地区')
    def select_address(self):
        allure.attach('选择所在地区', '选择所在地区')
        self.click_element(page.aolai_address)
        self.click_element(page.aolai_beijing1)
        self.click_element(page.aolai_beijing2)
        self.click_element(page.aolai_dongchengqu)

    @allure.step('输入详细地址')
    def input_detail_address(self, detail_address):
        allure.attach('输入详细地址', '输入详细地址')
        self.input_edit_content(page.aolai_detail_address, detail_address)

    @allure.step('输入邮编')
    def input_post_code(self, post_code):
        allure.attach('输入邮编', '输入邮编')
        self.input_edit_content(page.aolai_post_code, post_code)