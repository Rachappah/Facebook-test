'''
Created on 19/03/2017

@author: Rachappa
'''
from selenium import webdriver
import time
from lib2to3.tests.support import driver
if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("https://www.facebook.com/")
    driver.find_element_by_id("u_0_1").send_keys("rachappa")
    driver.find_element_by_id("u_0_3").send_keys("halinge")
    driver.find_element_by_id("u_0_6").send_keys("7353249488")
    time.sleep(1)
    driver.find_element_by_id("u_0_9").send_keys("7353249488")
    time.sleep(1)
    driver.find_element_by_id("u_0_d").send_keys("rach222")
    element=driver.find_element_by_id("day")
    e1=element.click()
    element.send_keys("6")
    element.click()
    time.sleep(1)
    element=driver.find_element_by_id("month")
    e2=element.click()
    element.send_keys("sep")
    element.click()
    element=driver.find_element_by_id("year")
    e3=element.click()
    element.send_keys("1990")
    element.click()
    driver.find_element_by_id("u_0_l").click()
    driver.find_element_by_id("u_0_h").click()
    
    
    
    
