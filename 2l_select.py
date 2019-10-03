from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
   
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element_by_xpath ("//span[@id ='num1']")
    a = num1.text
    print("Значение а: ", a)
   
    num2 = browser.find_element_by_xpath ("//span [@id ='num2']")
    b = num2.text
    print("Значение b: ", b)
    x = str(int(a)+int(b))
    print("Сумма a+b= ", x)
   
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(x)
    button = browser.find_element_by_class_name ("btn")
    button.click()

finally:

    time.sleep (10)
    browser.quit()
