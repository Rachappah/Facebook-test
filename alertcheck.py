'''
Created on 21/03/2017

@author: Rachappa
'''
from selenium import webdriver
import time
if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("http://demo.guru99.com/V4/ ")
    time.sleep(1)
    driver.find_element_by_name("uid").send_keys("rac222")
    time.sleep(1)
    driver.find_element_by_name("password").send_keys("2222")
    driver.find_element_by_name("btnLogin").click()
    time.sleep(1)
    driver.switch_to_alert().accept()
    driver.find_element_by_xpath("//div[@class='http://demo.guru99.com/']").click()
    