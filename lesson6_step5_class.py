
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    inp_element = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    inp_element.click()
    
    
    input1_element = browser.find_element(By.CSS_SELECTOR, "input")
    input1_element.send_keys("Ivan")
    input2_element = browser.find_element(By.CSS_SELECTOR, '[name="last_name"]')
    input2_element.send_keys("Petrov")
    input3_element = browser.find_element(By.CSS_SELECTOR, '.city')
    input3_element.send_keys("Smolensk")
    input4_element = browser.find_element(By.CSS_SELECTOR, "#country")
    input4_element.send_keys("Russia")
    button_element = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_element.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

