from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value_x = browser.find_element_by_id("treasure")
    elem_x = value_x.get_attribute ("valuex")
    print("Значение: ", elem_x)
    assert elem_x is not None
    x = elem_x
    y = calc(x) 

    inputx = browser.find_element_by_xpath("//input[@id = 'answer']")
    inputx.send_keys(y)

    option1 = browser.find_element_by_id ("robotCheckbox")
    option1.click()

    rules= browser.find_element_by_id("robotsRule")
    rules.click()
    
    button_x = browser.find_element_by_class_name("btn")
    button_x.click()
   
finally:

    time.sleep(10)
    browser.quit()
