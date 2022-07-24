from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
#https://www.selenium.dev/documentation/webdriver/
def main():
    serv_obj=Service("Y:\Discord-QR-Scam-main\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    driver.get("https://soundcloud.com/discover")
    driver.find_element("id","onetrust-accept-btn-handler").click()
    blame=driver.find_element("name","q")
    blame.send_keys("Face")
    blame.send_keys(Keys.RETURN)
    driver.find_element("class","g-nav-link sc-link-primary searchOptions__navigationLink sc-text-h4").click()
    
    time.sleep(5)
    driver.close()
    
    
    
if __name__ == '__main__':
    main()
