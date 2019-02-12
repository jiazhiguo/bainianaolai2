"""
实现元素的定位
"""

#定义应用的包名和启动名
from selenium.webdriver.common.by import By
aolai_app_package = "com.yunmall.lc"
aolai_app_activity = "com.yunmall.ymctoc.ui.activity.MainActivity"
aolai_app_activity2 = "com.yunmall.ymctoc.ui.activity.LogonActivity"

#1.homoe页面
#1.1定位到我的
aolai_home_btn_my = By.ID,"com.yunmall.lc:id/tab_me"
aolai_home_btn_shopping_cart = By.ID,"com.yunmall.lc:id/tab_shopping_cart"

#2.注册页面
#2.1定位到已有账号 去登录
aolai_regist_btn_already_account = By.ID,"com.yunmall.lc:id/gotologon"

#3.登录页面
#3.1 定位到账号
aolai_login_edit_account = By.ID,"com.yunmall.lc:id/logon_account_textview"
#3.2 定位到密码
aolai_login_edit_password = By.ID,"com.yunmall.lc:id/logon_password_textview"
#3.3 定位到登录按钮
aolai_login_btn_login= By.ID,"com.yunmall.lc:id/logon_button"
#3.4 定位到关闭按钮
aolai_login_btn_close_login= By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"




#4.个人中心页面
#4.1 定位到左上角设置按钮
aolai_person_center_btn_left_setting= By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_layout"

#5 设置页面
#5.1 退出按钮
aolai_setting_btn_setting_logout= By.ID,"com.yunmall.lc:id/setting_logout"
#5.2 定位到弹框的确定按钮
aolai_setting_btn_dialog_confirm= By.ID,"com.yunmall.lc:id/ymdialog_right_button"

#6 定位toast
aolai_toast_pwd_error = By.XPATH,"//*[contains(@text,'密码错误')]"



# 新增收货地址

aolao_setting_btn = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
aolao_address_manager = By.XPATH,"地址管理"
aolao_add_address = By.XPATH,"新增地址"
# addressee,tel,address,detail_address,post_code
aolai_addressee = By.ID,"com.yunmall.lc:id/address_receipt_name"
aolai_tel = By.ID,"com.yunmall.lc:id/address_add_phone"
aolai_address = By.ID,"com.yunmall.lc:id/address_province"

aolai_beijing1 = By.XPATH,"北京市"
aolai_beijing2 = By.XPATH,"北京市"
aolai_dongchengqu = By.XPATH,"东城区"

aolai_detail_address = By.ID,"com.yunmall.lc:id/address_detail_addr_info"
aolai_post_code = By.ID,"com.yunmall.lc:id/address_post_code"
