import unittest
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import os
from time import sleep
from appium import webdriver
import time

class Login(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['app'] = os.path.abspath('/Users/sminq/Downloads/UserApp-v2.2.2-queuingSystem.apk')
        desired_caps["session-override"] = 'false'

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)

    def test_correct_signin(self):
        self.driver.find_element_by_id("com.sminq.userbug:id/tv_next").click()
        self.driver.find_element_by_id("com.sminq.userbug:id/tv_next").click()
        self.driver.find_element_by_id("com.sminq.userbug:id/tv_next").click()
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

        self.driver.find_element_by_id("com.sminq.userbug:id/edit_text_mobile_number").send_keys('7000000003')
        self.driver.find_element_by_id("com.sminq.userbug:id/button_login").click()
        self.driver.find_element_by_id("com.sminq.userbug:id/btn_enter_otp_manually").click()
        self.driver.find_element_by_id("com.sminq.userbug:id/edit_text_otp").send_keys(989898)
        self.driver.find_element_by_id("com.sminq.userbug:id/button_verify_account").click()

        self.driver.find_element_by_id("android:id/button1").click()

        print self.driver.find_element_by_id("com.sminq.userbug:id/tv_selected_city").get_attribute('text')

    def tearDown(self):
    	self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Login)
    unittest.TextTestRunner(verbosity=2).run(suite)
