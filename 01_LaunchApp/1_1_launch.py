import unittest
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import os
from time import sleep
from appium import webdriver
import time

class LaunchApp(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['app'] = os.path.abspath('/Users/sminq/Downloads/UserApp-v2.2.1-demo.sminq.com-debug (1).apk')

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)

    def test_launch(self):

        if self.driver.find_element_by_id("com.sminq.userbug:id/navigation_container"):
            print "\nPassed! Onboarding Screen found!"
        else:
            print "\nFailed! Onboarding not found"

        self.driver.find_element_by_id("com.sminq.userbug:id/tv_next").click()
        self.driver.find_element_by_id("com.sminq.userbug:id/tv_next").click()
        self.driver.find_element_by_id("com.sminq.userbug:id/tv_next").click()

        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

    # def tearDown(self):
    # 	self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(LaunchApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
