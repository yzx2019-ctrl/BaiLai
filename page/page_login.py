# -*- coding: utf-8 -*-
from base.base import Base
import page


class PageLogin(Base):

    # 点击退出更新
    def page_click_quit_Update(self):
        self.base_click_element(page.login_click_quit_update)

    # 点击我
    def page_click_my(self):
        self.base_click_element(page.login_click_my)

    # 点击已有账号 去登录
    def page_click_have_id_go_login(self):
        self.base_click_element(page.login_have_id)

    # 输入账号
    def page_input_username(self, username):
        self.base_input_element(page.login_input_username, username)

    # 输入密码
    def page_input_password(self, password):
        self.base_input_element(page.login_input_password, password)


    # 点击登录按钮
    def page_click_login_button(self):
        self.base_click_element(page.login_click_login_button)


    # 获取用户名
    def page_get_username(self):
        self.base_get_element_info(page.login_get_username)


    # 点击设置按钮
    def page_click_setting_button(self):
        self.base_click_element(page.login_click_setting_button)

    # 点击退出
    def page_ckick_logout(self):
        # 滑动屏幕到底部 找到退出按钮
        self.base_swipe_screen()
        # 判断 退出按钮是存在
        if self.base_element_is_exist(page.login_click_logout):
            # 如果退出按钮存在点击
            self.base_click_element(page.login_click_logout)
            # 点击 确认按钮
            self.base_click_element(page.login_click_right_button)

    # 获取我
    def page_get_my(self):
        self.base_get_element_info(page.login_click_my)

    # 组合登录操作
    def page_login(self, username, password):
        self.page_click_my()
        self.page_click_have_id_go_login()
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_button()
