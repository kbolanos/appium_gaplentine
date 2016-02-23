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
        sleep(3)
        textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
        sleep(3)

        # login credentials
        textfields[0].send_keys('gap')
        textfields[1].send_keys('android428')

        # assert
        self.assertEqual('gap', textfields[0].text)

        # login button
        self.driver.find_element_by_id("com.sage.mobile:id/btnLogin").click()
        sleep(5)

        # google button
        self.driver.find_element_by_id("android:id/button1").click()
        sleep(15)

        # all options
        self.driver.find_element_by_id("com.sage.mobile:id/buttonDrawerMenu").click()
        sleep(3)

        # client button
        self.driver.find_element_by_xpath(
            "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]").click()
        sleep(5)

        # new client button
        self.driver.find_element_by_id("com.sage.mobile:id/buttonActionBar").click()
        sleep(3)

        client_fields = self.driver.find_elements_by_class_name('android.widget.EditText')
        sleep(3)
        client_fields[0].click()
        client_fields[0].send_keys('GAP Client')
        client_fields[1].click()
        client_fields[1].send_keys('123456')
        client_fields[2].click()
        client_fields[2].send_keys('78910')
        client_fields[3].click()
        client_fields[3].send_keys('client@wearegap.com')
        client_fields[4].click()
        client_fields[4].send_keys('www.growthaccelerationpartners.com')
        client_fields[5].click()
        client_fields[5].send_keys('Ciudad Quesada')
        client_fields[7].click()
        client_fields[7].send_keys('Quesada')
        client_fields[8].click()
        client_fields[8].send_keys('AL')
        client_fields[9].click()
        client_fields[9].send_keys('21001')
        client_fields[10].click()
        client_fields[10].send_keys('CR')

        # radio button
        self.driver.find_element_by_id('com.sage.mobile:id/address_checkbox').click()

        # save client
        self.driver.find_element_by_id("com.sage.mobile:id/buttonActionBar").click()
        sleep(10)

        # asserts
        client_labels = self.driver.find_elements_by_class_name('android.widget.TextView')
        sleep(5)
        self.assertEqual('GAP Client', client_labels[1].text)
        self.assertEqual('123456', client_labels[5].text)
        self.assertEqual('78910', client_labels[6].text)
        self.assertEqual('client@wearegap.com', client_labels[9].text)
        self.assertEqual('www.growthaccelerationpartners.com', client_labels[10].text)

        icons = self.driver.find_elements_by_class_name('android.widget.ImageView')

        icons[0].click()
        sleep(2)

        icons[3].click()
        sleep(2)

        icons[4].click()
        sleep(2)

        icons[5].click()
        sleep(2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
unittest.TextTestRunner(verbosity=2).run(suite)
