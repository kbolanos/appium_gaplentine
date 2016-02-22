__author__ = 'kbolanos'

from appium import webdriver
import unittest
import os
from time import sleep

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
app = "%s/apk/sage_mobile.apk" % CURRENT_DIR


class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'PREVIEW - Google Nexus 5X - 6.0.0 - API 23-1080x1920'
        desired_caps['app'] = app
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_find_elements(self):
        sleep(5)
        textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
        sleep(3)
        textfields[0].send_keys('gap')
        textfields[1].send_keys('android428')

        self.assertEqual('gap', textfields[0].text)

        self.driver.find_element_by_id("com.sage.mobile:id/btnLogin").click()
        sleep(5)
        self.driver.find_element_by_id("android:id/button1").click()
        sleep(25)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
