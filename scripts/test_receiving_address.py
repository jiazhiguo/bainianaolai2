import pytest

import page
from base.init_driver import get_driver
from base.read_yaml import read_yaml_data
from page.address_page import AddressPage
from page.login_page import LoginPage
from page.navigation_page import NavigationPage


def get_test_login_data():
    login_list = []
    data = read_yaml_data("login_data.yaml")
    login_list.append((data["test_login_01"]["username"], data["test_login_01"]["password"]))
    print(login_list)
    return login_list


class TestAddress:
    def setup_class(self):
        # self.driver = get_driver(page.aolai_app_package, page.aolai_app_activity)
        # 1.初始化driver
        self.driver = get_driver(page.aolai_app_package, page.aolai_app_activity)
        # 2.初始化导航类
        self.navigation_page = NavigationPage(self.driver)
        self.address_page = AddressPage(self.driver)

    @pytest.mark.parametrize("username,password", get_test_login_data())
    def test_login(self, username, password):
        """
        登录
        :param username:
        :param password:
        :return:
        """
        # 1.点击我的
        self.navigation_page.get_home_page_obj().click_btn_my()
        # 2.点击已有账号 去登录
        self.navigation_page.get_regist_page_obj().click_btn_already_account()
        # 3 输入账号密码 登录
        self.navigation_page.get_login_page_obj().click_btn_login(username, password)

    def test_add_address(self):
        # self.address_page.click_setting_btn()
        # self.address_page.click_address_manager_btn()
        # self.address_page.click_add_address_btn()
        # self.address_page.input_addressee("")
        # self.address_page.input_addressee()

        pass

    def teardown_class(self):
        self.driver.quit()
