import unittest
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import os
from time import sleep
from appium import webdriver
import time

class SignUp(unittest.TestCase):
    def setUp(self):
        title = ""
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['app'] = os.path.abspath('/Users/sminq/Downloads/UserApp-v2.2.1-demo.sminq.com-debug (1).apk')
        desired_caps['noReset'] = 'true'

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)

    def test_incorrect_signup(self):
        self.driver.find_element_by_id("com.sminq.userbug:id/edit_text_mobile_number").send_keys('7000000000')
        self.driver.find_element_by_id("com.sminq.userbug:id/button_login").click()

        title = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.widget.TextView[1]").get_attribute('text')

        print "\n"+title

        if title == "Sign Up":
            print "\nFailed! New user registration."
        else:
            print "\nPassed! Incorrect sign up. User is already registered."

    # def tearDown(self):
    # 	self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SignUp)
    unittest.TextTestRunner(verbosity=2).run(suite)
