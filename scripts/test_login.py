# -*- coding: utf-8 -*-
from base.get_driver import get_driver
from page.page_login import PageLogin


class TestLogin(object):

    def setup(self):
        # 获取driver
        self.driver = get_driver()
        # 实例化 PageLogin
        self.pagelogin = PageLogin(self.driver)
        # 关闭更新提示框
        self.pagelogin.page_click_quit_Update()



    def teardown(self):
        # 关闭driver
        self.driver.quit()



    def test_login(self, username="itheima_test", password="itheima"):

        # 调用组合登录方法
        self.pagelogin.page_login(username, password)
        # 获取用户名
        msg = self.pagelogin.page_get_username()
        print(msg)
        try:
            # 断言
            assert  msg == "itheima_test"
        except AssertionError:
            # 截图
            self.pagelogin.base_screensh_image()
        # 点击设置
        self.pagelogin.page_click_setting_button()
        # 点击退出
        self.pagelogin.page_ckick_logout()
        try:
            msg1 = self.pagelogin.page_get_my()
            print(msg1)
            assert msg1 == "我"
        except AssertionError:
            # 截图
            self.pagelogin.base_screensh_image()
