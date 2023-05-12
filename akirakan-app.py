from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions();

prefs = {"download.default_directory" : "C:/Users/DOUBLE33/PycharmProjects/akirakan-1/downloaded"};
options.add_experimental_option("prefs",prefs);

service = Service('/chromedriver')
driver = webdriver.Chrome(service=service,options=options)

try:

    driver.get('https://www.browserstack.com/test-on-the-right-mobile-devices');

    downloadcsv= driver.find_element_by_css_selector('.icon-csv');

    gotit= driver.find_element_by_id('accept-cookie-notification');

    gotit.click();    

    downloadcsv.click();

    time.sleep(5)

    driver.close()

except:

     print("Invalid URL")