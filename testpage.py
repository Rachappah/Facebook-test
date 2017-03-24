'''
Created on 20/03/2017

@author: Rachappa
'''
from selenium import webdriver
import time

if __name__ == '__main__':
    driver=webdriver.Firefox()
    time.sleep(1)
    driver.get("https://my.naukri.com/account/createaccount")
    time.sleep(1)
    driver.find_element_by_xpath("//div[@class='icon fresher']").click()
    time.sleep(1)
    driver.find_element_by_id("fname").send_keys("rachappa")
    time.sleep(1)
    driver.find_element_by_id("email").send_keys("rachappa@gmail.com")
    driver.find_element_by_xpath("//div[@class='password']").send_keys("rac222")
    driver.find_element_by_xpath("//div[@class='hidePwd']")
    
    
    
    
    