# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
import time

class Base(object):

    # 出始化
    def __init__(self, driver):
        self.driver = driver


    # 查找元素方法(结合显示等待)
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver,
                            timeout=timeout,
                            poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击元素方法
    def base_click_element(self, loc):
        self.base_find_element(loc).click()

    # 输入元素方法
    def base_input_element(self, loc, value):
        self.base_find_element(loc).send_keys(value)

    # 获取元素信息方法
    def base_get_element_info(self, loc):
        return self.base_find_element(loc).text

    # 判断一个元素是否存在方法
    def base_element_is_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=5)
            return True   # 代表元素存在页面中
        except:
            return False  # 代表元素不存页面中

    # 滑动屏幕方法
    def base_swipe_screen(self):
        self.driver.swipe(100, 2000, 100, 300)


    # 屏幕截图
    def base_screensh_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))