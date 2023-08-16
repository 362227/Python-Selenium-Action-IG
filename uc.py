#安装：pip3.8 install undetected-chromedriver
#wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
#yum install -y google-chrome-stable_current_x86_64.rpm


from pyvirtualdisplay import Display
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
import os
import sys
import requests

os.system("pkill -9 chrome")
os.system('killall chrome')

path = ChromeDriverManager().install()

if requests.get(sys.argv[1]).status_code == 200:
    page = requests.get(sys.argv[1])
    pageSource = page.content.decode('utf-8')
    print(pageSource)
else:
    display = Display(visible=0, size=(800, 600))
    display.start()

    class Demo:
        def set_chrome_option(self):
            chrome_options = uc.ChromeOptions()
            # chrome_options.headless = True
            chrome_options.add_experimental_option('prefs', {'profile.default_content_setting_values': {'notifications': 2}})
            chrome_options.add_argument('disable-infobars')
            chrome_options.add_argument('--proxy-server=http://127.0.0.1:1085')
            chrome_options.add_argument("--window-size=1920,1080")
            # chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('blink-settings=imagesEnabled=false')
            chromedriver_path = '/usr/local/bin/chromedriver'
            
            return chrome_options

        def run_all(self):
            try:
                                browser = uc.Chrome(executable_path=path, options=chrome_options)
                browser.get(sys.argv[1])  #网站
                browser.implicitly_wait(200)
                pageSource = browser.page_source
                print(pageSource)
            finally:
                browser.quit()

        def main(self):
            self.run_all()

    if __name__ == "__main__":
        demo = Demo()
        demo.main()

    exit()
    display.stop()
os.system('pkill -9 python')
