# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

"""以下为登录模块元素配置信息"""
# 点击退出更新
login_click_quit_update = By.ID, "com.yunmall.lc:id/img_close"
# 点击我
login_click_my = By.ID, "com.yunmall.lc:id/tab_me"
# 点击已有账号
login_have_id = By.ID, "com.yunmall.lc:id/textView1"
# 输入账户
login_input_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 输入密码
login_input_password = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 点击登陆按钮
login_click_login_button = By.ID, "com.yunmall.lc:id/logon_button"
# 获取账号
login_get_username = By.ID, "com.yunmall.lc:id/tv_user_nikename"
# 点击设置按钮
login_click_setting_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 点击退出
login_click_logout = By.ID, "com.yunmall.lc:id/setting_logout"
# 点击提示框确定按钮
login_click_right_button = By.ID, "com.yunmall.lc:id/ymdialog_right_button"