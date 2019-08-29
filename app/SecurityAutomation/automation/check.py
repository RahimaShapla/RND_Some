from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from string import Template
import unittest, json

CHROMEDRIVER = './chromedriver'
GRUYERE_ID = '932695469192'
TESTID_PREFIX = '444'  # int

urls = ["""http://google-gruyere.appspot.com/${GID}/${INPUT}"""]
payloads = ["""<script>console.error(${TID})</script>""",
            """console.error(${TID})//<svg/onload=console.error(${TID})>'-console.error(${TID})-'"""]


class XSSTest(unittest.TestCase):
    def setUp(self):
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ALL'}
        chrome_options = Options()
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-xss-auditor")
        self.driver = webdriver.Chrome(CHROMEDRIVER, chrome_options=chrome_options)

    def tearDown(self):
        self.driver.quit()

    def test_run(self):
        id = int(TESTID_PREFIX) * 10;
        for url in urls:
            for xss in payloads:
                xss1 = Template(xss).substitute(TID=str(id))
                url1 = Template(url).substitute(GID=GRUYERE_ID, INPUT=xss1)
                print
                url1
                id = id + 1
                self.driver.get(url1)
        self.result()

    def result(self):
        n = 0
        for cmsg in self.driver.get_log('browser'):
            if -1 != str(cmsg).find(" " + TESTID_PREFIX):
                print(json.dumps(cmsg))
                n += 1

        self.assertEqual(0, n)


# entry point
if __name__ == "__main__":
    unittest.main()