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
        desired_caps['app'] = os.path.abspath('/Users/sminq/Downloads/UserApp-v2.2.1-demo.sminq.com-debug (1).apk')
        desired_caps['noReset'] = 'true'

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)

    def test_correct_signin_pin(self):

        #Logout
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.RelativeLayout[1]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.support.v7.app.ActionBar.Tab[4]/android.widget.RelativeLayout[1]").click()

        self.driver.find_element_by_id("com.sminq.userbug:id/btn_logout").click()
        self.driver.find_element_by_id("android:id/button1").click()

        self.driver.find_element_by_id("com.sminq.userbug:id/edit_text_mobile_number").send_keys('1234567890')
        self.driver.find_element_by_id("com.sminq.userbug:id/button_login").click()
        self.driver.find_element_by_id("com.sminq.userbug:id/edit_text_pin").send_keys(1111)

        if self.driver.find_element_by_id("com.sminq.userbug:id/tv_selected_city"):
            print "\nPassed! Sign in successful"
            print self.driver.find_element_by_id("com.sminq.userbug:id/tv_selected_city").get_attribute('text')
        else:
            print "\nFailed! Sign in unsuccessful"


    # def tearDown(self):
    # 	self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Login)
    unittest.TextTestRunner(verbosity=2).run(suite)
